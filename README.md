# FluHost-AA

FluHost-AA is a reproducible computational platform for host-associated amino-acid analysis of publicly available naturally occurring Influenza A virus sequences.

## Runtime Architecture

- Windows, VS Code, and Codex are the repository editing and control plane.
- GitHub is the source of truth for repository contents and history.
- Kaggle is the canonical runtime for Python execution, testing, and scientific computation.
- Scientific analysis code, parameters, and large data artifacts are introduced only through later project phases.

The repository is organized into contracts, configuration, source, tests, Kaggle notebook snapshots, manifests, reports, workflows, and project documentation.

## Kaggle Notebook Workflow

Kaggle is the development, interactive debugging, and execution environment for notebooks. GitHub's `kaggle/notebooks/` directory stores only frozen snapshots of validated Kaggle Notebook versions that completed Run All and Save Version. Draft, working, debugging, and prototype-in-progress notebooks are not part of the formal archive.

The canonical Python and project sources remain in `src/`, `tests/`, `configs/`, and `contracts/`. Kaggle code datasets or working directories must be generated from those sources; duplicate notebook copies are not maintained as implementation sources.
