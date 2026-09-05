from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Tuple
import hashlib
import json

import numpy as np
import pandas as pd
from Bio import SeqIO
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests

VALID_HOSTS = {"Avian", "Human"}
STANDARD_AA = set("ACDEFGHIKLMNPQRSTVWY")


@dataclass(frozen=True)
class PB2Config:
    exclude_gap: bool = True
    exclude_x: bool = True
    gap_char: str = "-"
    x_char: str = "X"


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_metadata(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() == ".parquet":
        df = pd.read_parquet(path)
    else:
        sep = "\t" if path.suffix.lower() in {".tsv", ".txt"} else ","
        df = pd.read_csv(path, sep=sep)

    required = {"sequence_id", "host_group"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required metadata columns: {sorted(missing)}")
    if df["sequence_id"].duplicated().any():
        dup = df.loc[df["sequence_id"].duplicated(), "sequence_id"].head().tolist()
        raise ValueError(f"Duplicate sequence_id in metadata, examples: {dup}")
    bad_hosts = sorted(set(df["host_group"].dropna()) - VALID_HOSTS)
    if bad_hosts:
        raise ValueError(f"Unexpected host_group values: {bad_hosts}")
    return df.copy()


def load_fasta(path: str | Path) -> Dict[str, str]:
    seqs: Dict[str, str] = {}
    for rec in SeqIO.parse(str(path), "fasta"):
        sid = rec.id
        if sid in seqs:
            raise ValueError(f"Duplicate FASTA id: {sid}")
        seqs[sid] = str(rec.seq).upper()
    if not seqs:
        raise ValueError("FASTA contains no sequences")
    return seqs


def validate_aligned(seqs: Dict[str, str]) -> int:
    lengths = {len(s) for s in seqs.values()}
    if len(lengths) != 1:
        raise ValueError(f"Sequences are not aligned: observed lengths={sorted(lengths)[:10]}")
    return next(iter(lengths))


def intersect_inputs(metadata: pd.DataFrame, seqs: Dict[str, str]) -> Tuple[pd.DataFrame, Dict[str, str], dict]:
    meta_ids = set(metadata["sequence_id"])
    fasta_ids = set(seqs)
    common = meta_ids & fasta_ids
    if not common:
        raise ValueError("No sequence_id overlap between metadata and FASTA")
    m = metadata[metadata["sequence_id"].isin(common)].copy()
    s = {k: seqs[k] for k in m["sequence_id"]}
    report = {
        "metadata_rows": len(metadata),
        "fasta_records": len(seqs),
        "matched_records": len(common),
        "metadata_without_fasta": len(meta_ids - fasta_ids),
        "fasta_without_metadata": len(fasta_ids - meta_ids),
    }
    return m, s, report


def aa_frequency_table(metadata: pd.DataFrame, seqs: Dict[str, str], cfg: PB2Config) -> pd.DataFrame:
    aln_len = validate_aligned(seqs)
    host_by_id = metadata.set_index("sequence_id")["host_group"].to_dict()
    rows = []
    for pos0 in range(aln_len):
        by_host = {"Avian": {}, "Human": {}}
        denominators = {"Avian": 0, "Human": 0}
        for sid, seq in seqs.items():
            host = host_by_id[sid]
            aa = seq[pos0]
            if cfg.exclude_gap and aa == cfg.gap_char:
                continue
            if cfg.exclude_x and aa == cfg.x_char:
                continue
            denominators[host] += 1
            by_host[host][aa] = by_host[host].get(aa, 0) + 1

        observed = sorted(set(by_host["Avian"]) | set(by_host["Human"]))
        for aa in observed:
            a = by_host["Avian"].get(aa, 0)
            h = by_host["Human"].get(aa, 0)
            rows.append({
                "alignment_position": pos0 + 1,
                "aa": aa,
                "avian_count": a,
                "human_count": h,
                "avian_denominator": denominators["Avian"],
                "human_denominator": denominators["Human"],
                "avian_frequency": a / denominators["Avian"] if denominators["Avian"] else np.nan,
                "human_frequency": h / denominators["Human"] if denominators["Human"] else np.nan,
            })
    out = pd.DataFrame(rows)
    out["delta_frequency"] = out["human_frequency"] - out["avian_frequency"]
    return out


def add_association_stats(freq: pd.DataFrame) -> pd.DataFrame:
    out = freq.copy()
    odds = []
    ps = []
    for r in out.itertuples(index=False):
        a = int(r.human_count)
        b = int(r.human_denominator - r.human_count)
        c = int(r.avian_count)
        d = int(r.avian_denominator - r.avian_count)
        or_val, p = fisher_exact([[a, b], [c, d]], alternative="two-sided")
        odds.append(or_val)
        ps.append(p)
    out["odds_ratio"] = odds
    out["fisher_p"] = ps
    if len(out):
        out["fdr_bh"] = multipletests(out["fisher_p"].fillna(1.0), method="fdr_bh")[1]
    else:
        out["fdr_bh"] = []
    return out



def requested_residue_row(
    table: pd.DataFrame,
    position: int,
    aa: str,
    position_col: str = "alignment_position",
) -> pd.DataFrame:
    """Return one position/residue row, including an explicit zero-count row if absent.

    This is useful for predefined reproduction anchors: absence of the requested
    residue should be reported as frequency 0 rather than as a missing result.
    """
    aa = aa.upper()
    hit = table[(table[position_col] == position) & (table["aa"] == aa)].copy()
    if len(hit):
        return hit

    pos_rows = table[table[position_col] == position]
    if pos_rows.empty:
        raise ValueError(f"Position {position} is absent from table")

    avian_den = int(pos_rows["avian_denominator"].iloc[0])
    human_den = int(pos_rows["human_denominator"].iloc[0])
    synthetic = pd.DataFrame([{
        position_col: position,
        "aa": aa,
        "avian_count": 0,
        "human_count": 0,
        "avian_denominator": avian_den,
        "human_denominator": human_den,
        "avian_frequency": 0.0 if avian_den else np.nan,
        "human_frequency": 0.0 if human_den else np.nan,
        "delta_frequency": 0.0 if avian_den and human_den else np.nan,
    }])
    return add_association_stats(synthetic)


def anchor_65d(table: pd.DataFrame, position_col: str = "reference_position") -> pd.DataFrame:
    if position_col not in table.columns:
        position_col = "alignment_position"
    return table[(table[position_col] == 65) & (table["aa"] == "D")].copy()


def write_manifest(path: str | Path, payload: dict) -> None:
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
