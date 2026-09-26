# Methods and analytical status

The table separates **project-reported Kaggle runtime validation** from evidence committed to this repository. No HA code, run record, QC summary, output manifest, or statistical result is currently committed here for independent verification. Runtime validation does not establish scientific validation or approve an undocumented parameter. The [frozen project scope contract](contracts/project/scope_v1.0.yaml) governs allowed work; the separate [F0 contract](contracts/science/f0_legacy_baseline_v1.0.yaml) remains draft with historical choices `TBD`.

| Stage | Activity | Status |
| --- | --- | --- |
| HA dataset reconstruction | Reconstruct the public HA sequence dataset | Project-reported completed and runtime-validated in Kaggle; supporting artifacts are not committed here |
| HA alignment and mapping | Subtype-specific MSA and reference-position mapping | Project-reported completed and runtime-validated in Kaggle; reference and QC details are not committed here |
| HA descriptive frequencies | All-subtype Human vs Avian amino-acid frequencies and within-subtype Human minus Avian frequency differences | Project-reported completed and runtime-validated in Kaggle; tables and run evidence are not committed here |
| HA site assessment | Site prioritization, H1/H3 detailed validation and visualization, statistical association testing, and cross-subtype consistency | In progress; no completed downstream validation is claimed |
| Robustness | Temporal, geographic, lineage, and phylogeny-aware validation | Planned; no completed validation is claimed |
| Expanded context | Reassortment context and genome constellations; leakage-aware temporal and held-out ML benchmarks | Planned |
| F0 historical baseline | Recover historical choices and outputs, reproduce recoverable results, and record discrepancies | Separate reproduction phase; draft contract and `TBD` parameters |

Governed choices include host ontology, inclusion and exclusion rules, deduplication, QC, reference sequence and numbering, statistical tests and correction, sampling, lineage definitions, and validation splits. They require proposal -> PI review -> contract update -> implementation. No choice is inferred from a reported runtime result. Core logic should reside in reusable package functions under `src/`, with notebooks under `kaggle/` orchestrating them. See [reproducibility](docs/reproducibility.md) and the [validation evidence inventory](reports/validation/README.md).
