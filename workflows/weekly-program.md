# weekly-program

One honest RAID and one status page. No new facts in the deck.

## When to use

A recurring program or project pulse.

## When not to use

A scope/date/design change — run `assess-change` and do not bury it in status.

## Inputs

- Existing `docs/govern/raid.md` if any
- Git / CI evidence for the window
- `context/decision-rights.md`

## Outputs

- Updated RAID
- Blocker triage (ids in RAID)
- `docs/govern/status-YYYY-MM-DD.md`

## Steps

1. Skill: `update-raid`  
   Agent profile: `coordinator`  
   Stop if: a new row has no source
2. Skill: `triage-blockers`  
   Agent profile: `coordinator`
3. Skill: `write-status`  
   Agent profile: `coordinator`  
   Stop if: a progress line has no RAID / git / CI / artifact citation
4. Skill: `draft-steerco` only if a steerco pack is needed this week  
   Agent profile: `coordinator`  
   Stop if: it would add a fact not in status or RAID
5. **Human gate:** Program manager sets RAG and sends the page

## Failure

Invented green → rewrite. Missing RAID → status must say RAID missing, not “on track.”

## Done

- [ ] Status path exists
- [ ] RAG is human-set
- [ ] Every highlight/slip cites a source
