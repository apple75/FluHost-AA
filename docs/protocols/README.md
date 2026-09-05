# Protocols

Document operational protocols here.

## Current F1.1 Migration

- [F1.1 status](f1_1_status.md) records the historical engineering smoke-test status.
- Kaggle is the F1.1 notebook development and execution environment.
- A F1.1 notebook enters the GitHub archive only after Kaggle Run All and Save Version; the saved version is a frozen snapshot, not the development source.
- The F1.1 implementation source remains canonical in `src/`, `tests/`, `configs/`, and `contracts/`.
- Formal F1.1 results are not established by migrated local or pre-platform outputs; they require a later Kaggle Save Version and artifact download.