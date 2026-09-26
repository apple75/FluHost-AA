# Roadmap

This is a status map, not a schedule or claim of scientific validation. The [methods page](METHODS.md) separates project-reported Kaggle runtime validation from evidence available in GitHub.

| Status | Work |
| --- | --- |
| Reported completed and runtime-validated in Kaggle | HA public dataset reconstruction, subtype-specific MSA, reference-position mapping, all-subtype Human vs Avian amino-acid frequencies, and within-subtype frequency differences. Supporting run records and outputs are not committed here. |
| In progress | HA site prioritization; H1/H3 detailed validation and visualization; statistical association testing; cross-subtype consistency. |
| Planned | Temporal, geographic, lineage, and phylogeny-aware validation; reassortment-context analysis; leakage-aware ML generalization benchmarks under approved splits. |
| Separate F0 phase | Historical baseline reproduction under the [draft F0 contract](contracts/science/f0_legacy_baseline_v1.0.yaml); recover historical assets and resolve `TBD` choices through review before claiming F0 PASS. |

The next reproducibility milestone is to add shareable lightweight QC summaries, manifests, code and configuration references, and validation reports tied to fixed commits, without adding restricted or large raw datasets. See [reports/validation](reports/validation/README.md) for the missing Stage07 and Stage08B evidence categories.
