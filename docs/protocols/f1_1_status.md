# FLUHOST-F1.1 — PB2 Public Smoke Dataset & First Run

Status: **PASS**

## Dataset
- Source: public `jbloomlab/PB2-DMS` GitHub repository
- Upstream file: `compareS009/compareS009_avian_human.faa`
- Upstream repository license: GPL-3.0
- Records: 10 (5 Avian + 5 Human)
- PB2 length: 759 aa
- Purpose: engineering smoke test only

## First-run results
- metadata/FASTA matching: 10/10
- alignment length: 759
- association rows: 823
- pytest: 2 passed
- PB2 position 65, residue D in this fixture:
  - Avian frequency: 0.00%
  - Human frequency: 0.00%

This zero frequency is expected for this tiny fixture and is not a reproduction-quality comparison with the dissertation's historical FLUDB cohort.

## Gate
F1.1 engineering smoke test: **PASS**

Next: F1.2 — construct a larger public PB2 Avian/Human dataset from NCBI for a meaningful reproduction-oriented run.
