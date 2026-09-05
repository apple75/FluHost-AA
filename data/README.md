# Data Directory

Large scientific datasets are not stored in Git.

Current canonical scientific runtime and primary data storage platform:
Kaggle.

Logical data stages:

raw
-> interim
-> processed
-> analysis-ready
-> results

Raw source data must be immutable.

Formal frozen datasets must be identified using:
- dataset ID
- version
- manifest
- SHA256 checksums
- provenance

Small synthetic or public test fixtures may be stored under:
tests/fixtures/