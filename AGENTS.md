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

FluHost-AA is a computational and observational research project based on
publicly available, naturally occurring Influenza A virus sequences.

The project does not include:

- design of novel influenza viruses
- synthetic viral genome design
- optimization of pathogenicity
- optimization of transmissibility
- optimization of host range
- optimization of immune escape
- design of novel reassortant viruses
- virus rescue protocols
- virus culture or propagation protocols
- infection protocols
- serial-passage or adaptation protocols
- experimental procedures intended to enhance viral fitness

Analysis of naturally observed variants, sequence frequencies, phylogenies,
lineages, reassortment histories, and host-associated statistical signals is
within scope.

If a requested task crosses this boundary, stop only the out-of-scope part and
continue any unaffected computational or documentation work.


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

## 12. Instruction and scientific-contract precedence

AGENTS.md governs agent behavior.

Approved files under `contracts/` define the current scientific rules and
analysis contracts.

README files and other documentation are descriptive and MUST NOT silently
override an approved scientific contract.

If an instruction, implementation, README, notebook, configuration file, or
historical artifact appears to conflict with an approved scientific contract:

1. do not resolve the conflict silently
2. do not modify the scientific contract automatically
3. report the conflict explicitly
4. identify the affected files and governed parameters
5. wait for PI review when a scientific-rule change would be required

Historical artifacts may document older behavior but do not automatically
override the current approved contract.


## 13. Public-repository and external-review policy

This repository may be used as a public research record and as supporting
material for researcher-access or trusted-access review.

Public-facing documentation must be factual and verifiable.

Agents MUST NOT invent or imply:

- institutional affiliations
- registered legal entities
- researcher identities
- ORCID identifiers
- grants or funding
- publications
- DOIs
- ethics approvals
- regulatory approvals
- institutional endorsements
- collaborations
- laboratory capabilities
- experimental results

If such information is required but not present in the repository, use an
explicit placeholder such as:

- `[RESEARCHER NAME]`
- `[CONTACT EMAIL]`
- `[ORCID, IF APPLICABLE]`
- `[INSTITUTION, IF APPLICABLE]`

Do not convert a project name, research brand, or informal group name into a
claim that it is a registered company, institution, or legal entity.


## 14. Explicit research boundary

FluHost-AA is a computational and observational research project based on
publicly available, naturally occurring Influenza A virus sequences.

The project does not include:

- design of novel influenza viruses
- synthetic viral genome design
- optimization of pathogenicity
- optimization of transmissibility
- optimization of host range
- optimization of immune escape
- design of novel reassortant viruses
- virus rescue protocols
- virus culture or propagation protocols
- infection protocols
- serial-passage or adaptation protocols
- experimental procedures intended to enhance viral fitness

Analysis of naturally observed variants, sequence frequencies, phylogenies,
lineages, reassortment histories, and host-associated statistical signals is
within scope.

If a requested task crosses this boundary, stop only the out-of-scope part and
continue any unaffected computational or documentation work.


## 15. Data licensing, redistribution and privacy

Public availability does not automatically imply unrestricted redistribution.

Before committing or publishing data, check the applicable source terms.

In particular:

- NCBI and other public resources should retain provenance and accession
  information where appropriate.
- GISAID-derived sequence data must not be redistributed in violation of
  GISAID terms.
- Third-party datasets must retain required attribution and licensing terms.
- Personal, confidential, clinical, credential, or account information must
  not be committed.
- API keys, tokens, cookies, passwords, private URLs, and other secrets must
  never be committed.

When in doubt, commit code, schemas, manifests, checksums and documentation
instead of restricted raw data.


## 16. Formal reproducibility requirements

A formal scientific result should be traceable to:

- a fixed Git commit or release tag
- an approved scientific contract
- explicit configuration
- input dataset identity and version
- input manifest
- SHA256 checksums where applicable
- runtime environment
- commands or notebook execution steps
- output manifest
- QC results
- PASS/FAIL acceptance criteria

Lightweight result summaries may be committed when appropriate.

Large generated scientific outputs should normally remain in Kaggle datasets,
release assets, or another approved data store rather than Git.


## 17. Current project priority

The current primary analysis priority is host-associated amino-acid analysis
of Influenza A HA sequences using naturally occurring public sequence data.

Current workflow emphasis includes:

1. subtype-specific sequence analysis
2. reference-position mapping
3. Human vs Avian amino-acid frequency analysis
4. host-associated statistical signals
5. cross-subtype validation
6. temporal and geographic validation
7. phylogeny-aware validation

Multi-segment PB2/PB1/PA/NP/NA/M/NS analysis remains part of the broader
roadmap but should not be treated as the current default analysis target unless
explicitly requested.


## 18. Public documentation quality gate

Before preparing a public release or documentation-focused commit, agents
should check:

- project purpose is understandable without private context
- research boundaries are explicit
- statistical association is not presented as causality
- current project status is accurate
- no unsupported biological claims are introduced
- no private or restricted data are included
- no credentials or secrets are present
- no institutional or legal claims are invented
- Markdown links are valid where practical
- repository structure matches the documented structure
- placeholders requiring manual completion are clearly reported

A documentation task is not complete merely because Markdown files were
created. Public-facing statements must remain consistent with the scientific
contracts and actual project state.