# F1.1 Smoke Dataset Provenance

Purpose: engineering smoke test only; not a scientifically representative dataset.

Source:
- Public GitHub repository: `jbloomlab/PB2-DMS`
- File: `compareS009/compareS009_avian_human.faa`
- Repository license: GNU GPL v3.0
- The source file contains PB2 protein sequences whose FASTA headers explicitly encode `_HOST_Avian_` or `_HOST_Human_`.

Selection:
- 5 Avian records + 5 Human records were selected for a deterministic smoke-test fixture.
- No biological ranking or phenotype-based selection was used.
- The fixture is intentionally too small for scientific inference.

Use:
- Validate parsing, accounting, amino-acid frequency calculation, Fisher test, FDR, and output generation.
- Do NOT compare this 10-sequence fixture numerically with the dissertation's full FLUDB cohort as evidence of reproduction quality.


## Public source verification

The source repository is public and the repository metadata reports GNU GPL v3.0.
The upstream analysis notebook explicitly filters FASTA records containing
`_HOST_Human_` or `_HOST_Avian_`, and the upstream repository contains the
derived protein FASTA `compareS009_avian_human.faa`.

This F1.1 fixture contains only 10 records copied from that public file to
exercise the software pipeline. It is not the dissertation cohort and must not
be used for scientific conclusions.
