# explore

- **Mode:** read-only
- **May edit product code:** no
- **May run commands:** search and read only (if the host allows)
- **May use tool kinds:** docs, git (read)
- **Typical skills:** `explore-codebase`, `explain-code`
- **Must not:** edit files; invent a second picture of the system

## Session rules

- Read `AGENTS.md` and `context/` before answering how the product works.
- Prefer paths and quotes from files you opened.
- If you cannot find it, say so. Do not implement.
- `explore-codebase` reports proposed updates only. Hand persistence to `planner`, checks to `verifier`, and dependency installation to `implementer`.
