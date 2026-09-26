# Validation Reports

This directory is reserved for lightweight validation evidence. No Stage07 or Stage08B run summary, QC report, or output manifest is currently committed. The stage labels themselves are not defined in this repository, so their exact relationship to the reported HA workflow must be supplied by the researcher before publication.

For **each** of Stage07 and Stage08B, add a shareable QC summary and a run/output manifest after verifying the source records. Suggested filenames are `stage07_qc_summary.md`, `stage07_run_manifest.yaml`, `stage08b_qc_summary.md`, and `stage08b_run_manifest.yaml`; these files do not exist yet.

Each summary should state the stage purpose, exact Git commit, Kaggle notebook or command and run identifier, approved contract and configuration references, dataset identifier and version, input and output manifests, SHA256 checksums where applicable, host/subtype counts, exclusions and QC counts, tests performed, acceptance criteria, actual outcome, and discrepancies. Include alignment, reference-mapping, or frequency-table QC only when that stage actually produced it. Link to authorized storage for larger outputs instead of committing raw FASTA, restricted data, or large result files. Do not label a stage PASS without its required runtime and scientific validation evidence.
