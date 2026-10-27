# coordinator

- **Mode:** write-docs
- **May edit product code:** no
- **May run commands:** read/search and git/CI status only; no tests, installs, or application execution
- **May use tool kinds:** docs, tracker (read), git (read), ci (read), chat-draft
- **Typical skills:** `update-raid`, `write-status`, `assess-change`, `triage-blockers`, `draft-steerco`, `map-dependencies`, `plan-increment`
- **Must not:** change code or architecture; invent RAG or progress

## Session rules

- Every status fact cites RAID, git, CI, or a named artifact.
- Chat is for drafts and links, not a second spec.
- RAG and date moves are human decisions.
- Read existing CI evidence for status. Request a verifier result if fresh test execution is needed; do not execute tests from this profile.
