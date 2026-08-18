# Agent profiles

Permission envelopes, not job titles. Map each file onto whatever the host calls a role, permission mode, or sub-session. See [agent-standard](../docs/reference/agent-standard.md).

| Profile | Mode | Must not |
| --- | --- | --- |
| [explore](explore.md) | read-only | edit files |
| [planner](planner.md) | write-docs | implement product code |
| [shaper](shaper.md) | write-docs | change product code |
| [implementer](implementer.md) | write-code + execute | merge; prod deploy |
| [reviewer](reviewer.md) | read-only | edit the diff it reviews |
| [verifier](verifier.md) | execute tests | delete or skip a failing test |
| [releaser](releaser.md) | execute; prod gated | unattended prod; money; account changes |
| [coordinator](coordinator.md) | write-docs | change code or architecture |
| [incident-lead](incident-lead.md) | read runtime + write incident doc | silent prod changes |

UI and backend developers both use `implementer`. Optional writer/reviewer overlays: [personas/](personas/).
