# FluHost-AA

**FluHost-AA is a reproducible computational bioinformatics project for studying host-associated amino-acid statistical signals in publicly available, naturally occurring Influenza A virus sequences.**

The current research focus is **hemagglutinin (HA) Human vs Avian comparative analysis**, with emphasis on distinguishing stable host-associated sequence signals from subtype, lineage, temporal, geographic, and phylogenetic confounding.

The project is designed for comparative genomics, molecular epidemiology, One Health surveillance, and reproducible computational research.

---

## Research objectives

FluHost-AA investigates questions such as:

- Which amino-acid residues show stable Human vs Avian frequency differences?
- Which signals remain consistent across influenza subtypes?
- Which signals remain stable across time and geography?
- Which associations remain after accounting for lineage and phylogenetic structure?
- How robust are host-associated sequence signals under lineage-disjoint and temporal validation?

Results are interpreted as **statistical associations**, not automatic causal biological effects.

Preferred terminology includes:

- host-associated amino-acid signal
- host-associated residue
- statistical association
- frequency difference
- cross-subtype consistency
- temporal stability
- geographic stability
- phylogenetic robustness
- naturally occurring variant

---

## Current HA workflow

The current HA analysis pipeline includes:

1. public-sequence dataset reconstruction
2. metadata normalization
3. quality control and deduplication
4. subtype-specific multiple sequence alignment
5. subtype-specific reference-position mapping
6. Human vs Avian amino-acid frequency analysis
7. Human minus Avian frequency-difference analysis
8. host-associated site prioritization
9. cross-subtype validation
10. temporal and geographic validation
11. phylogeny-aware association analysis

### Current status

The project reports these stages as completed and runtime-validated in Kaggle:

- HA public dataset reconstruction
- subtype-specific HA multiple sequence alignment
- subtype-specific reference-position mapping
- all-subtype Human vs Avian amino-acid frequency analysis
- within-subtype Human minus Avian frequency-difference analysis

Run logs, output manifests, and validation reports for these stages are not yet present in this repository for independent review.

Current work focuses on:

- host-associated site prioritization
- H1/H3 detailed validation and visualization
- statistical association testing
- cross-subtype consistency analysis

Later phases include:

- temporal validation
- geographic validation
- phylogeny-aware association
- reassortment-context analysis
- temporal and lineage-disjoint machine-learning benchmarks

Runtime-dependent workflows are currently executed in **Kaggle**, which is the canonical scientific runtime for the project.

---

## Research boundaries

FluHost-AA is a **computational and observational research project** based on naturally occurring viral sequences.

The project does **not** aim to:

- design novel influenza viruses
- generate synthetic viral genomes
- optimize pathogenicity
- optimize transmissibility
- optimize host range
- optimize immune escape
- design novel reassortant viruses
- develop virus rescue protocols
- develop viral propagation or culture protocols
- develop infection protocols
- develop serial-passage or adaptation protocols

The project analyzes naturally observed sequence variation and does not engineer or experimentally modify viruses.

---

## Data sources

Primary data sources may include:

- NCBI / GenBank
- NCBI Influenza resources
- BV-BRC
- public research datasets and repositories
- legally authorized scientific datasets

Formal analyses should record data provenance, dataset versions, manifests, and checksums.

Data governed by redistribution restrictions are not published in this repository in violation of their terms.

Large raw sequence datasets are not stored directly in Git.

---

## Reproducibility

FluHost-AA uses a GitHub + Kaggle workflow:

- **GitHub** — source of truth for code, contracts, configuration, documentation, tests, manifests, and releases
- **Kaggle** — canonical runtime for routine scientific workflows and reproducibility runs
- **HPC** — reserved for future analyses that require substantially larger compute resources

Formal analyses should be traceable to:

- a fixed Git commit or release tag
- an approved scientific contract
- explicit configuration
- dataset identity and version
- input manifests
- SHA256 checksums
- runtime information
- QC reports
- output manifests

See [Reproducibility](docs/reproducibility.md).

---

## Scientific governance

Scientific parameters are governed and are not changed silently.

Governed parameters include:

- host ontology
- inclusion and exclusion criteria
- deduplication rules
- QC thresholds
- reference sequence
- reference numbering
- statistical tests
- multiple-testing correction
- sampling strategy
- lineage definitions
- temporal splits
- benchmark splits

Changes follow:

**Proposal → PI Review → Contract Update → Implementation**

See:

- [Project scope](RESEARCH_SCOPE.md)
- [Safety and governance](SAFETY_AND_GOVERNANCE.md)
- [Scientific interpretation](docs/scientific_interpretation.md)

---

## Historical reproduction

The project also contains an **F0 historical baseline reproduction phase**.

F0 aims to reproduce documented historical analytical choices before methodological modernization.

Unknown historical parameters remain explicitly marked as `TBD` rather than being replaced with modern defaults.

Relevant contracts:

- [Project scope contract](contracts/project/scope_v1.0.yaml)
- [F0 historical baseline contract](contracts/science/f0_legacy_baseline_v1.0.yaml)

Historical reproduction and current methodological development are treated as separate scientific tasks.

---

## Repository structure

| Path | Purpose |
| --- | --- |
| `contracts/` | Governed project scope and scientific parameters |
| `configs/` | Runtime configuration separate from scientific contracts |
| `data/` | Data-stage documentation; large raw datasets are not stored in Git |
| `manifests/` | Dataset and result provenance records |
| `src/` | Reusable scientific software |
| `tests/` | Automated tests |
| `kaggle/` | Kaggle runtime assets and notebooks |
| `workflows/` | Scientific workflow definitions |
| `reports/` | Lightweight validation and analysis reports |
| `docs/` | Architecture, methods, interpretation, reproducibility, and project documentation |

---

## Documentation

Start here:

- [Project overview](docs/project_overview.md)
- [Research scope](RESEARCH_SCOPE.md)
- [Methods](METHODS.md)
- [Data sources](DATA_SOURCES.md)
- [Safety and governance](SAFETY_AND_GOVERNANCE.md)
- [Scientific interpretation](docs/scientific_interpretation.md)
- [Reproducibility](docs/reproducibility.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

---

## Project status

FluHost-AA is under active development.

Current work covers HA site prioritization, H1/H3 validation and visualization, statistical testing, and cross-subtype consistency analysis. Temporal and phylogeny-aware validation remain later phases.

---

## Contact

Researcher: `Guoping Tan`

Contact: `gptan@hhu.edu.cn`
