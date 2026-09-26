# Access and safety governance for proposed GPT-Rosalind use

This document describes controls required **before** any GPT-Rosalind deployment for FluHost-AA. It is not evidence that FluHost-AA has GPT-Rosalind access, an approved organization, an enterprise workspace, or operating security controls. The repository currently establishes the computational research boundary, scientific-contract change process, and prohibition on committing secrets and restricted data through [AGENTS.md](../AGENTS.md) and the [scope contract](../contracts/project/scope_v1.0.yaml). No access roster, access administrator, safety owner, or incident procedure is committed here.

| Control | Required practice if access is approved | Evidence still needed from the applicant |
| --- | --- | --- |
| Approved users | Grant access only to named users with a defined need for the approved computational use case; record approval and review the roster. | Authorized user roster, approving authority, and onboarding record. |
| Least privilege | Limit workspace, model, repository, dataset, and API permissions to each user's approved tasks. Keep privileged administration separate from routine research access. | Workspace/API roles, permission configuration, and review record. |
| Revocation | Remove access when a user leaves, changes role, loses the approved need, or is involved in suspected misuse; record who acted and when. | Offboarding procedure, responsible administrator, and revocation evidence. |
| Safety oversight | Name one person accountable for safety decisions, scope review, and escalation. Scientific parameter changes still follow the contract review process. | `[RESPONSIBLE SAFETY OWNER]`, authority, and a reachable reporting route. |
| Misuse and security incidents | Provide a private route to report suspected out-of-scope use, account compromise, data exposure, or credential loss. Triage, contain access, preserve appropriate records, notify the responsible owner and provider when required, and document closure. | Incident contact, response procedure, escalation authority, and reporting obligations. |
| Credential protection | Do not commit or share passwords, tokens, API keys, cookies, or private URLs. Use approved secret storage and rotate or revoke exposed credentials. | Secret-storage and account-security controls; evidence of access review. |

Do not upload restricted source data, personal information, or confidential material to a model or tool without source-term and access review. Raw data remain immutable. Only the [proposed use case](gpt_rosalind_use_case.md) is in scope; the [safety boundary](../SAFETY_AND_GOVERNANCE.md) remains authoritative for project conduct.

OpenAI's current [GPT-Rosalind access guidance](https://help.openai.com/en/articles/20001193-gpt-rosalind-for-life-sciences-research) and [deployment system card](https://deploymentsafety.openai.com/gpt-rosalind-5-5) describe approved-user, least-privilege, revocation, and organizational oversight expectations. Eligibility and verification are OpenAI decisions, not repository claims.
