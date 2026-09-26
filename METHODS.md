# Methods and analytical status

This page describes the analytical program, not a completed or approved parameter set. The [project scope contract](contracts/project/scope_v1.0.yaml) defines allowed work. Governed choices such as host ontology, inclusion criteria, QC, references, statistical tests, and splits require the proposal -> PI review -> contract update -> implementation process. No missing choice is inferred here. The planned HA focus does not determine F0's target segment or other historical parameters; those remain `TBD` in the F0 contract.

| Stage | Intended analysis | Current status |
| --- | --- | --- |
| F0 historical baseline | Recover the thesis data, choices, and outputs; reproduce recoverable results and record discrepancies | Draft [F0 contract](contracts/science/f0_legacy_baseline_v1.0.yaml); historical assets and parameters `TBD` |
| HA preparation | Validate metadata and sequences, subtype-specific MSA, and reference-position mapping | Planned; reference and QC choices require approved contracts |
| Association | Compare Human vs Avian amino-acid frequencies within subtypes, with contract-approved statistical tests and multiplicity handling | Planned; host ontology and tests are not yet specified |
| Robustness | Assess cross-subtype consistency, temporal and geographic stability, and phylogenetic robustness | Planned; strata and methods require approval |
| Context and generalization | Analyze reassortment context and genome constellations; evaluate ML with temporal, lineage, subtype, or geographic holdouts and leakage checks | Planned; benchmarks and splits require approval |

Core analysis belongs in reusable package functions under `src/`; notebooks under `kaggle/` should orchestrate them. Formal results require versioned data provenance, recorded configuration, runtime validation in Kaggle, and interpretation as statistical association. See [reproducibility](docs/reproducibility.md).
