# FluHost-AA

FluHost-AA is a reproducible computational platform for host-associated amino-acid analysis of publicly available naturally occurring Influenza A virus sequences.

## Runtime Architecture

- Windows, VS Code, and Codex are the repository editing and control plane.
- GitHub is the source of truth for repository contents and history.
- Kaggle is the canonical runtime for Python execution, testing, and scientific computation.
- Scientific analysis code, parameters, and large data artifacts are introduced only through later project phases.

The repository is organized into contracts, configuration, source, tests, Kaggle entry points, manifests, reports, workflows, and project documentation.

## F1.1 Kaggle Entry Points

- Engineering smoke baseline: `kaggle/notebooks/f1_1/pb2_f1_1_first_smoke_run.ipynb`
- Prototype / later-stage reference: `kaggle/notebooks/prototype/pb2_scientific_prototype.ipynb`

The canonical Python source is `src/fluhost_pb2.py`. Kaggle code datasets or working directories must be generated from that source; duplicate copies are not maintained in this repository. The F1.1 notebook does not read `configs/pb2_prototype.yaml`; that file remains prototype configuration and does not control the F1.1 run.
