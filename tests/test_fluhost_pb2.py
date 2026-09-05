import pandas as pd
from src.fluhost_pb2 import PB2Config, aa_frequency_table, add_association_stats, requested_residue_row

def test_frequency_and_stats():
    meta = pd.DataFrame({
        "sequence_id": ["a1", "a2", "h1", "h2"],
        "host_group": ["Avian", "Avian", "Human", "Human"],
    })
    seqs = {"a1": "AA", "a2": "AD", "h1": "DD", "h2": "DA"}
    freq = aa_frequency_table(meta, seqs, PB2Config())
    row = freq[(freq.alignment_position == 1) & (freq.aa == "D")].iloc[0]
    assert row.avian_frequency == 0.0
    assert row.human_frequency == 1.0
    out = add_association_stats(freq)
    assert {"odds_ratio", "fisher_p", "fdr_bh"} <= set(out.columns)


def test_requested_absent_residue_is_explicit_zero():
    meta = pd.DataFrame({
        "sequence_id": ["a1", "h1"],
        "host_group": ["Avian", "Human"],
    })
    seqs = {"a1": "AE", "h1": "AE"}
    assoc = add_association_stats(aa_frequency_table(meta, seqs, PB2Config()))
    row = requested_residue_row(assoc, position=2, aa="D").iloc[0]
    assert row.avian_count == 0
    assert row.human_count == 0
    assert row.avian_frequency == 0.0
    assert row.human_frequency == 0.0
