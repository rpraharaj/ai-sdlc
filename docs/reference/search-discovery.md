# Search discovery and README positioning

Reviewed: 2026-10-28. Scope: the source README and repository discovery copy. This is an editorial plan, not evidence of indexing, rankings, or traffic.

## Evidence and limits

- A current search sample for AI SDLC and software-development agent skills returned repositories describing skill packs, frameworks, and lifecycle workflows, including [eniga/agent-skills](https://github.com/eniga/agent-skills) and [huanrasan/sdlc-harness](https://github.com/huanrasan/sdlc-harness). This supports using recognizable terminology; it does not establish search volume, competition scores, or ranking feasibility. The README wording is original and based on this repository's actual files.
- The SEO keyword-research report returned `PROVIDER_UNAVAILABLE`. No keyword-volume estimates were obtained. No Search Console or Analytics data for this repository was used.
- Google's [Search Essentials](https://developers.google.com/search/docs/essentials) recommends helpful content and the words people use to find it in prominent headings and descriptive links. Its [title-link guidance](https://developers.google.com/search/docs/appearance/title-link) recommends descriptive, concise titles and avoids keyword stuffing. These principles support the README's explicit title, short definition, task table, and linked examples; they do not promise rankings.
- GitHub controls the rendered repository page and its HTML metadata. Editing a Markdown heading is not the same as setting an independent page's HTML title or meta description. The README work did not create a hosted site. On 2026-10-28, the repository description and eight topics below were applied to [rpraharaj/ai-sdlc](https://github.com/rpraharaj/ai-sdlc) and verified by reading the repository settings back.

## Candidate topics and reader intent

These are qualitative candidates, not validated high-volume keywords:

| Topic | Reader's likely question | Existing answer |
| --- | --- | --- |
| AI SDLC / AI-assisted software development lifecycle | What is this project and how does it help a team? | README definition, workflow, and audience |
| AI agent skills for software development | Which reusable procedures are included? | Task table and linked skill catalog |
| AGENTS.md and SKILL.md workflows | Where do context and procedures live? | README components and portability reference |
| AI-assisted requirements, testing, and code review | How do roles hand work to each other? | Skill examples and artifact chain |
| Human approval gates for coding agents | What still needs a person, and what is enforced? | Oversight section and pilot checklist |

Keep the README focused on orientation and adoption. Keep detailed procedures in their existing skill and reference homes; link to them instead of duplicating all 66 skills or creating thin pages for wording variants.

## Applied repository metadata

The following description and topics were approved and applied on 2026-10-28. The homepage remains a separate recommendation:

- **About description:** Open-source AI SDLC pack: 66 vendor-neutral agent skills, context templates, and workflows for requirements, code, testing, review, and release.
- **Topics:** `ai-sdlc`, `agent-skills`, `ai-assisted-development`, `software-development-lifecycle`, `spec-driven-development`, `agents-md`, `developer-tools`, `developer-workflow`.
- **Homepage:** use a real maintained documentation URL only if one exists. Do not invent a hosted site or publish a duplicate README without a clear purpose.

GitHub's [repository-topics guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) explains how topics help people find related projects. Topics are a discovery aid, not a guarantee of Google rankings.

## Verify after publication

1. Review the rendered README on GitHub for heading structure, table readability, code blocks, and relative-link resolution. Run `python3 scripts/check-pack.py` locally before publishing.
2. Confirm the visible repository description/topics and public accessibility. A successful source push or metadata update does not demonstrate search-engine indexing.
3. Record a dated baseline for a small set of candidate queries using a consistent market and device. Search-result samples are observations, not search-demand estimates.
4. Use repository traffic data and first-party search data where actually available. Keep measurement windows and source limitations explicit; do not attribute changes in visits solely to the README rewrite.
5. Publish a real pilot example or case study only after evidence exists, with permission for any program information. Describe what was observed and its limits; avoid invented adoption claims or productivity gains.

A future documentation website could provide controlled page metadata, crawl/indexing configuration, and Search Console measurement on an owned property. It is separate work requiring an actual hosting/domain decision; this README update does not create that site.
