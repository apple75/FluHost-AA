# Reproducibility

GitHub is the source of truth for code, contracts, configuration, tests, documentation, and releases. Kaggle is the canonical Python and scientific runtime in this project phase. Windows, VS Code, and Codex serve as the editing and control plane. HPC and WSL2 are optional future runtimes under the project scope contract; HPC use would require a scale justification. Static inspection cannot establish runtime success.

For each formal analysis, record the exact Git commit or release tag; approved contract and configuration versions; dataset identifier, version, source provenance, manifest, and SHA256 checksums; runtime environment and commands or notebook steps; expected inputs and outputs; tests and their actual results; and discrepancies or exclusions with counts. Keep raw inputs immutable and store large data outside Git.

F0 requires faithful recovery of historical choices and a discrepancy register. Its [draft contract](../contracts/science/f0_legacy_baseline_v1.0.yaml) leaves key inputs and parameters `TBD`. A formal F0 PASS requires the evidence specified by that contract, including Kaggle execution and frozen provenance. Until then, describe work as implemented or statically reviewed only when supported, not as runtime or scientific validation.

See [data sources](../DATA_SOURCES.md), [methods](../METHODS.md), and [manifests](../manifests/README.md).
