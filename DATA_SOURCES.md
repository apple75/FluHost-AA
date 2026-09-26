# Data sources and governance

The [project scope contract](contracts/project/scope_v1.0.yaml) permits NCBI, BV-BRC, public research datasets, and legally authorized research data. GISAID is conditional on its data-use and redistribution requirements; GISAID-restricted records must not be added to this public repository. No dataset snapshot, download date, accession list, or source-specific selection rule has yet been established here.

Raw source data are immutable. Large sequence and processed datasets belong outside Git, in the authorized analysis environment. Git may contain small suitable fixtures, schemas, manifests, checksums, code, and lightweight summaries. Do not commit credentials, personal information, confidential files, or restricted data.

For a formal frozen dataset, record its identifier and version, source and provenance, manifest, SHA256 checksums, and the code commit used. Document retrieval and redistribution constraints for each source. Dataset identity must be independent of a Kaggle slug. See [reproducibility](docs/reproducibility.md) and [data directory guidance](data/README.md).
