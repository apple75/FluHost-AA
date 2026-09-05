# FLUHOST-F1 — Kaggle PB2 Scientific Prototype Freeze

Status: FROZEN v1
Scope: Computational analysis of publicly available, naturally occurring influenza A PB2 protein sequences.

## 1. Scientific objective

Reproduce the computational logic of Chapter 3, Section 2.1 of Guo Yanna's 2023 doctoral dissertation at the PB2-only level, and quantify concordance with published PB2 summary anchors.

The prototype is observational. It identifies amino-acid states statistically associated with host origin in public natural sequences. It does not infer that a statistical association is causal.

## 2. Dissertation-derived anchors

The dissertation states that:
- sequences were collected from FLUDB for avian-origin and human-origin influenza A viruses before 2021;
- MAFFT was used for sequence alignment;
- homologous/duplicate sequences were removed;
- BioEdit was used to calculate amino-acid proportions at each position;
- Table 3-6 reports PB2 counts after filtering: Avian = 21,041; Human = 31,137;
- PB2 position 65, residue D: Avian = 3.95%; Human = 36.26%;
- known markers such as PB2 E627K and D701N were excluded before the paper selected its final per-gene top candidates.

The exact original FLUDB snapshot, accession list, detailed definition of "homologous/duplicate", and a fully executable ranking formula are not available in the dissertation text. Therefore exact result identity is NOT a Phase-1 acceptance requirement.

## 3. Phase-1 scope

IN:
1. PB2 only.
2. Avian vs Human only.
3. Protein consensus sequences and metadata.
4. Deterministic QC.
5. Multiple-sequence alignment input or optional MAFFT execution.
6. Reference-position mapping.
7. Per-position amino-acid counts and frequencies.
8. Delta frequency.
9. Odds ratio and Fisher exact test.
10. Benjamini-Hochberg FDR.
11. Dissertation-anchor comparison.
12. Versioned output manifest.

OUT:
- PB1, PA, NP.
- subtype/year/geography stratification.
- phylogenetic analysis.
- wet-lab analysis.
- causal claims about host adaptation.
- mutation-combination optimization.

## 4. Input contract

Required metadata columns:
- sequence_id: unique key matching FASTA record id
- host_group: exactly Avian or Human

Recommended metadata:
- accession
- strain_name
- subtype
- collection_date
- year
- country
- source_database

Sequence input:
- PB2 amino-acid FASTA
- either pre-aligned, or unaligned if MAFFT is available in the Kaggle runtime

## 5. QC contract

For F1:
- sequence_id must be unique in metadata;
- FASTA ids must be unique;
- only host_group in {Avian, Human};
- sequence must contain standard amino-acid characters plus X/gap as configured;
- exact duplicate sequences may be removed only when explicitly enabled;
- every removal must be counted and reported;
- no hidden/manual deletions.

No additional biological QC threshold may be invented by the agent.

## 6. Statistical contract

For each reference-mapped PB2 position and each observed amino acid:
- n_avian_residue
- n_avian_other
- n_human_residue
- n_human_other
- avian_frequency
- human_frequency
- delta_frequency = human_frequency - avian_frequency
- odds_ratio from Fisher's exact test
- fisher_p
- fdr_bh

Gap and X handling must be explicit and recorded in the run manifest.

## 7. Dissertation reproduction gates

G1 Pipeline integrity:
- notebook completes from validated inputs to result tables;
- tests pass.

G2 Dataset accounting:
- raw and retained Avian/Human counts are reported.
- differences from dissertation Table 3-6 are quantified, not silently corrected.

G3 PB2-65D anchor:
- platform reports Avian and Human frequencies for reference position 65 residue D;
- compare against 3.95% and 36.26%;
- report absolute percentage-point deviations.

G4 Full-position result:
- produce complete PB2 host-association table.

G5 Modern statistics:
- OR/Fisher/FDR columns produced for all tested position-residue pairs.

G6 Reproducibility:
- save config, input hashes, software versions, timestamp and result hashes.

## 8. Acceptance rule

F1 is PASS when G1–G6 are all present and reproducible.

Exact equality with the dissertation's PB2 top-candidate list is not required at F1 because the original data snapshot and exact ranking rule are not fully specified.

## 9. Safety / interpretation boundary

Use terms:
- host-associated signal
- host-associated residue
- frequency difference
- statistical association

Do not automatically translate association into:
- increased pathogenicity
- increased transmissibility
- expanded host range
- causal host adaptation

## 10. Next phase

Only after F1 PASS:
F2 = dataset reconstruction refinement + paper-like ranking rule audit.
