# Decision rights

Who decides. Skills draft; they do not take these decisions.

| Decision | Human role | AI may | AI must not |
| --- | --- | --- | --- |
| Problem / success for a product change | Product manager | Draft the PRD | Invent users, metrics, or “this is approved” |
| Must vs Should and the requirements baseline | Business owner + BA | Propose a split and draft requirements | Promote Should to Must or accept the baseline without human evidence |
| Irreversible tech choice | Solution architect | Draft the ADR | Record the choice as decided without a signer |
| Date move, funding, kill a workstream | Program manager | Draft impact (`assess-change`) | Change the plan as if accepted |
| Go-live | Product + DevOps (or the row you name) | Draft the go/no-go pack | Deploy or declare live |
| Production change | Named on-call / releaser | Draft the runbook and rollback | Unattended prod access |
| Money / cloud account | Human in the billing account | Explain what the human would do in a dashboard | Purchase, upgrade, or change the account |
| Legal / compliance | Named counsel or compliance owner | List open questions | Invent a legal rule |

Replace role titles with the real names or team aliases this program uses. Add rows; do not delete the money / production / legal rows.

## Approval evidence

- **Approval home:** `(unknown)` — name the existing decision log, review record, or the table below. Do not create a second approval system.
- An approval identifies the decision, artifact path and exact revision (commit or content digest), human signer, date, outcome, and evidence link. Release approvals also identify the environment and release revision.
- A status label such as `accepted`, a reviewer name, or an AI session is not approval evidence. Until the authorized human's decision is evidenced, record `unassigned` and stop the dependent work.
- A waiver records the specific check or prerequisite, reason, human authorized by the decision table, evidence, revision, and expiry or scope. The agent may draft it; it must not grant it.
- Changes to approved scope, acceptance, contracts, approach, release revision, or environment invalidate the affected approval and downstream checks. Obtain approval again for the changed revision. Editorial changes may retain approval only when the signer explicitly defined that scope.
- Approval permits only the named action. It does not grant production credentials or expand a session's permission profile. For this template's go-live row, a human performs the production deployment.

| Decision / waiver | Artifact / release | Revision | Environment or n/a | Human signer | Date | Outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |
