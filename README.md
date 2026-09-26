# FluHost-AA

**FluHost-AA is a computational bioinformatics project** studying host-associated amino-acid statistical signals in publicly available, naturally occurring Influenza A virus sequences. Its current focus is hemagglutinin (HA) Human vs Avian analysis. Planned methods include subtype-specific multiple sequence alignment (MSA), reference-position mapping, amino-acid frequency analysis, temporal and geographic validation, phylogeny-aware analysis, reassortment-context analysis, and machine-learning (ML) generalization benchmarks.

**Interpretation and boundary:** Results describe statistical associations and frequency differences, not automatic causal biological effects. The project does not design, engineer, or optimize viruses.

**Current status:** This repository is a research and reproducibility scaffold. The [project scope contract](contracts/project/scope_v1.0.yaml) is frozen; the [F0 historical baseline contract](contracts/science/f0_legacy_baseline_v1.0.yaml) is a draft with unresolved `TBD` parameters. No scientific result or runtime validation is claimed here. F0 aims to reproduce documented historical choices before later methodological development.

## Start here

- [Project overview](docs/project_overview.md) and [research scope](RESEARCH_SCOPE.md)
- [Methods and phase status](METHODS.md) and [roadmap](ROADMAP.md)
- [Data sources](DATA_SOURCES.md), [safety and governance](SAFETY_AND_GOVERNANCE.md), and [scientific interpretation](docs/scientific_interpretation.md)
- [Reproducibility requirements](docs/reproducibility.md) and [contributing](CONTRIBUTING.md)

## Repository map

| Path | Purpose |
| --- | --- |
| `contracts/` | Governed project scope and scientific parameters |
| `configs/` | Runtime configuration, separate from scientific contracts |
| `data/` and `manifests/` | Data-stage guidance and provenance records; no large raw datasets in Git |
| `src/` and `tests/` | Package and test structure for future implementation |
| `kaggle/` and `workflows/` | Canonical runtime entry points and phase workflows |
| `reports/` | Validation and phase reports when available |
| `docs/` | Architecture, decisions, protocols, troubleshooting, and public guides |

GitHub is the source of truth for versioned code and documentation. Kaggle is the current canonical runtime for Python tests and scientific workflows; a fixed commit or release tag is required for formal reproducibility runs. See [reproducibility](docs/reproducibility.md).
