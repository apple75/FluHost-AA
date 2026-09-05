# FluHost-AA Agent Instructions

## 1. Project scope

FluHost-AA is a reproducible computational bioinformatics platform for analysis of publicly available, naturally occurring Influenza A virus sequences.

The project focuses on:

* host-associated amino-acid statistical signals
* subtype-aware analysis
* temporal validation
* geographic validation
* lineage-aware analysis
* phylogeny-aware association
* reassortment-aware multi-segment analysis
* temporal and lineage-disjoint machine-learning benchmarks
* reproducible scientific software and data infrastructure

The project does not design or optimize new viral variants.

## 2. Current execution architecture

The current project architecture is:

* Windows + VS Code + Codex: repository editing and control plane
* GitHub: source of truth for code, contracts, configuration, tests, documentation and releases
* Kaggle: canonical runtime for Python execution, tests, scientific workflows and routine computation
* HPC: optional future compute environment only when justified by scale

Do not assume that a local Python, Conda, MAFFT, IQ-TREE or scientific runtime exists on the Windows host.

Runtime-dependent validation must be performed in Kaggle unless explicitly stated otherwise.

Static inspection alone is not sufficient to mark a runtime-dependent task as PASS.

## 3. Scientific governance

The following scientific parameters are governed and MUST NOT be changed silently:

* host ontology
* inclusion criteria
* exclusion criteria
* deduplication rules
* QC thresholds
* reference sequence
* reference numbering
* statistical tests
* multiple-testing correction
* sampling strategy
* lineage definitions
* temporal splits
* benchmark splits
* causal interpretation terminology

Required change process:

Proposal -> PI Review -> Contract Update -> Implementation

If implementation appears to require changing a governed scientific parameter, stop that part of the implementation and report the issue.

Do not infer missing scientific parameters.

Do not substitute modern defaults for undocumented historical choices.

Unknown values must remain explicitly UNKNOWN or TBD until resolved.

## 4. Scientific interpretation

Default project outputs represent statistical association, not causal biological effects.

Preferred terminology includes:

* host-associated amino-acid signal
* host-associated residue
* statistical association
* frequency difference
* cross-subtype consistency
* temporal stability
* geographic stability
* phylogenetic robustness
* naturally occurring variant
* candidate site for further investigation
* reassortment context
* genome constellation

Do not automatically describe an observed association as causing:

* host adaptation
* increased transmissibility
* increased pathogenicity
* increased fitness
* immune escape

unless the statement is explicitly supported by cited published evidence.

## 5. Data policy

Raw data must be treated as immutable.

Do not modify raw source files in place.

Large scientific datasets do not belong in Git.

GitHub should contain:

* code
* contracts
* schemas
* configuration
* tests
* small fixtures
* documentation
* manifests
* checksums
* lightweight result summaries when appropriate

Kaggle datasets may contain:

* FASTA files
* metadata tables
* Parquet files
* frozen public-data snapshots
* reusable processed datasets

Every frozen dataset used in a formal analysis should eventually have:

* dataset identifier
* dataset version
* manifest
* SHA256 checksums
* provenance information

## 6. Engineering rules

Prefer reusable Python package functions over notebook-only implementations.

Core scientific logic must not exist only inside notebooks.

Notebooks should orchestrate package functions and present results.

Avoid duplicated scientific logic.

Use explicit configuration.

Do not introduce unexplained magic numbers.

Validate inputs before analysis.

Fail explicitly on invalid or ambiguous inputs.

Prefer deterministic processing.

Where randomness is required, use explicit seeds controlled by an approved configuration or scientific contract.

Use pathlib-compatible paths and avoid user-specific absolute paths.

Core package code must not depend directly on a specific Kaggle dataset slug.

## 7. Kaggle runtime policy

Kaggle is the canonical runtime during the current project phase.

Code written in VS Code may be reviewed statically, but runtime-dependent claims require Kaggle execution.

For runtime-dependent changes, report:

* Kaggle commands or notebook steps required
* expected inputs
* expected outputs
* tests that must run
* PASS/FAIL criteria
* runtime assumptions

Do not claim that tests passed unless actual test output is available.

Development runs may use a branch or development commit.

Formal reproducibility runs must use a fixed Git commit or release tag.

## 8. Agent editing workflow

Before editing:

1. inspect the repository
2. inspect the closest applicable AGENTS.md
3. inspect relevant scientific contracts
4. inspect relevant tests
5. identify files expected to change
6. identify whether governed scientific parameters are involved

During editing:

1. make the smallest coherent change
2. avoid unrelated refactoring
3. do not change contracts unless explicitly instructed
4. add or update tests when implementation behavior changes
5. preserve raw inputs

After editing:

1. summarize files changed
2. summarize behavior changed
3. identify tests required
4. distinguish static review from runtime validation
5. report unresolved issues
6. report any assumptions
7. do not commit unless explicitly instructed

## 9. F0 legacy baseline rule

F0 is a historical reproduction phase.

Its objective is to faithfully reconstruct the historical thesis baseline before methodological modernization.

For F0:

* preserve documented historical choices
* do not silently modernize methods
* do not replace historical parameters with contemporary defaults
* record discrepancies rather than forcing results to match
* mark unknown historical choices explicitly
* separate reproduction from later methodological improvement

Historical reproduction and scientific modernization are separate tasks.

## 10. Prohibited silent behavior

Agents must not silently:

* change scientific contracts
* alter raw data
* change reference numbering
* change statistical methods
* change QC thresholds
* redefine host groups
* redefine subtype inclusion
* modify benchmark splits
* suppress failed tests
* ignore missing values
* drop records without reporting counts
* hard-code personal machine paths
* treat Kaggle dataset names as scientific dataset identities
* claim PASS without the required validation evidence

## 11. Definition of implementation completion

A code edit is not automatically a completed scientific task.

Use these states where appropriate:

* IMPLEMENTED: code change exists
* STATICALLY REVIEWED: source/diff inspection completed
* TESTED: required automated tests executed
* RUNTIME VALIDATED: required Kaggle workflow executed
* SCIENTIFICALLY VALIDATED: outputs checked against the approved scientific contract
* PASS: all task-specific acceptance criteria are satisfied

Do not collapse these states into a single unsupported PASS claim.
