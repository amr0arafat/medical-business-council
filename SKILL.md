---
name: medical-business-council
description: Use when a hospital, clinic, medical school, or research-center leader wants a non-clinical business or administrative decision debated by a council of Silicon Valley operators (Bezos, Andy Grove, Reed Hastings, Satya Nadella, Elon Musk, Bill Gates, plus on-call Jobs, Collison, Doerr, Horowitz, Huang) and a Governance Guardian with veto power. Triggers - "medical business council", "convene the council", "take this to the board", "run this policy past the council", "what would Bezos/Grove do with our hospital", or a real tradeoff about admin policy, staffing, procurement, budgets, grants office, KPIs/OKRs, AI adoption, reorganization, outsourcing, revenue, or bureaucracy reduction. Three rounds, then a scored verdict with dissent and a 30-day plan. Also one-seat consults ("ask the Grove seat") and building new evidence-grounded advisors. NOT for patient-level clinical decisions.
version: 0.2.0
author: Amr Arafat
license: MIT
argument-hint: "[the decision] [--quick] [--all] [--seats grove,hastings,...] | ask <seat> [question] | board | build <name>"
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [council, healthcare-administration, hospital-management, research-administration, policy, subagents, roast-room]
    related_skills: [medical-research-council]
---

# Medical Business Council

A board meeting on one administrative or business decision for a hospital, clinic, medical faculty, or research center. Each seat is a sub-agent that reasons the way one Silicon Valley leader does, translated to healthcare administration. A **Governance Guardian** seat (a role, not a person) holds a veto, because "move fast and break things" breaks people and licenses in healthcare. You act as the **Chair**: you never argue a side, you run the room, keep the score, and write the verdict.

Inspired by [roast-room](https://github.com/nateherkai/roast-room) (three-round council, weighted scores, ruin cap, verbatim-quote checks).

Read once before the first run: `roster.json`, `references/seats.md` (lens cards, weights, tensions), `references/round-prompts.md`, `references/scoring.md`, `references/report-template.md`. A finished example lives in `examples/2026-10-31-example-procurement-approvals/`.

## Scope

In scope (anything about running the institution, not treating a patient):
- Admin policy and SOPs: approval chains, delegation of authority, leave, overtime, remote work, meeting rules.
- People: hiring, staffing models, performance systems, incentives, culture, reorganization, leadership changes.
- Operations: scheduling, bed/OR/clinic capacity as a business process, supply chain, procurement, outsourcing.
- Money: budgets, cost cutting, pricing of services and packages, new revenue lines, grants, philanthropy, PPPs.
- Research administration: grants office, core facilities, ethics committee throughput (the office, not the study), publication incentives, industry contracts, tech transfer.
- Digital and AI: ERP/HIS procurement, automation, AI for admin work, data governance programs.
- Strategy: partnerships, expansion, accreditation programs, branding, medical tourism.

Out of scope: diagnosis, treatment, a specific patient, clinical protocols, or study design. Say so in one line and point to the `medical-research-council` skill for clinical research and MedTech questions. A decision that touches patient data or patient experience at the policy level is in scope; the Guardian weighs it heavily.

## Tools by runtime

| Need | Claude Code | Hermes Agent |
|---|---|---|
| Ask the user | AskUserQuestion | `clarify` |
| Spawn seats in parallel | Agent tool, `general-purpose`, all seats in one message | `delegate_task`, all seats in one call |
| Read/write files | Read / Write | `read_file` / `write_file` |
| Run the quote checker | Bash `python3 ...` | `execute_code` |
| Web (build mode only) | WebSearch / WebFetch | `web_search` / `web_extract` |

`SKILL_DIR` below means this skill's folder. Sessions go in `./council-sessions/` under the user's current working directory.

## Modes

- **Full council** (default): five to seven seats plus the Guardian, three rounds. For expensive or hard-to-undo decisions.
- **Quick** (`--quick`): three seats plus the Guardian, Rounds 1 and 2, Round 3 only if scores did not converge. For reversible calls.
- **Named seats** (`--seats a,b,c`): those seats plus the Guardian, three rounds.
- **Everyone** (`--all`): every seat in `roster.json`, capped at nine plus the Guardian.
- **Consult** (`ask <seat> ...`): one seat, one answer, single-seat prompt. No scoring, no session folder.
- **Board settings** (`board`): show and change the default board. See "Board settings".
- **Build** (`build <name>`): build an evidence-grounded brain for a seat or a new advisor. Follow `references/build-advisor.md`.

## Brains and lens mode

Each seat can run two ways. Check `SKILL_DIR/brains/<slug>/_hot.md` for every seated advisor before Round 1.

- **Brain mode** (the brain exists): the seat reads its brain and may quote verbatim lines with source ids, like `"exact words" (S014)`. Quotes are checked in Step 7.
- **Lens mode** (no brain yet): the seat reasons from its lens card in `seats.md`. It may name a framework and where it comes from ("Type 1 and Type 2 decisions, 2015 shareholder letter") but **must not put the leader's words in quotation marks**. Everything is paraphrase in the seat's voice.

Tell the user in one line which seats ran in lens mode, and that `build <name>` upgrades a seat to brain mode. Never invent quotes, numbers, or stories about the real person in either mode.

## Pick the board

1. `--seats` or `--all` on this run wins. `--quick` then picks three from those.
2. Otherwise `"board"` in `roster.json` decides: `"ask"` (recommend and confirm), `"auto"` (recommend and seat, say who in one line), or `"default"` (seat the default list).
3. **The Guardian always sits.** It does not count toward the seat limits.

### Recommend a board

- Every seat whose pillar the decision lives in or materially affects (weight 2 or 3).
- The money seat (Gates) whenever the decision moves budget, revenue, or headcount.
- The seat most likely to disagree with the rest, so the council argues instead of nodding. `seats.md` lists natural tensions.
- Bring an on-call seat in when the decision is in its lane: Jobs (staff- or patient-facing service experience, simplification), Collison (research enterprise), Doerr (KPIs, OKRs, targets), Horowitz (layoffs, turnarounds, leadership crises), Huang (AI and org structure).
- Five to seven seats for a full council, three for `--quick`.

### Ask

Show the recommendation as a short list, one plain line per seat on why it fits, then one line naming who was left out. Then ask one question (header "Board"): **Recommended board (Recommended)**, **Default board**, **Everyone**. The user can type swaps. If Step 1 also needs facts, ask everything in the same call. If the user said "just run it", seat the recommendation.

## Step 1: The brief

Build it from what the user gave you. If any of the first four items is missing, ask for them in one batch (at most four questions). If the user says "just run it", fill gaps with stated assumptions.

1. **The decision** in one line, and the options as A, B, C. Always include "keep the current way", and add the obvious smaller version (a pilot in one department) if the user brought only one idea.
2. **The institution**: type (public, private, or university hospital, research center, clinic network), size (beds, staff, researchers), country and funding model, who decides and who must approve (board, ministry, university council, union).
3. **The resources and limits**: budget, deadline, headcount, procurement or civil-service rules, accreditation calendar.
4. **What success looks like**, as a number and a date where possible (turnaround days, cost per case, grant income, staff turnover, satisfaction score).
5. **Which way the user is leaning, and why.** The council tests the lean; it does not echo it.

Context lookup: if the working folder holds notes about the institution (a `CLAUDE.md`, `institution.md`, policy drafts, budget sheets), read them before asking. Keep the brief under 350 words and mark each assumption `(assumed)`.

## Step 2: Set up the room

- Seat the board. Give every seat (Guardian included) a relevance weight of 1 to 3 with a one-line reason, per `seats.md`.
- Create `./council-sessions/YYYY-MM-DD-<decision-slug>/` and save `brief.md` (brief, options, weights table, brain or lens mode per seat).
- Tell the user in one line who is at the table and that `--seats`, `--all`, or `board` change it.

## Step 3: Round 1, opening positions

Spawn every seat in **one message**, in parallel, foreground, with the Round 1 prompt from `round-prompts.md`. Each seat prompt starts with that seat's system block, built from `references/seat-template.md` and its lens card.

Save the cards verbatim to `round-1.md`, one `## <Seat short name>` heading per card. Send a card back once if it is missing scores, stance, or (for the Guardian) the veto line. Then add `## Chair notes`:

- The **cruxes**: one to three underlying disagreements (a factual, a numbers, or a values question such as speed versus staff wellbeing), with the seats on each side.
- The **unanimity check** (`scoring.md`). If it triggers and the strongest unargued alternative is a distinct plan, add it as a new scored option (D) and assign seats to argue and answer it, per "Chair-added options" in `scoring.md`. One added option at most.
- Any card that broke format, misread the brief, or drifted into clinical advice.

## Step 4: Round 2, debate

Spawn every seat again in one message with the Round 2 prompt (it points them at `brief.md` and `round-1.md`). Save to `round-2.md` with `## Chair notes`: who moved and why, which cruxes resolved, which numbers are still open, interim option scores, and the Guardian's current veto status.

## Step 5: Draft resolution

Write `draft-resolution.md`: the recommended option and verdict label, the merged conditions (each checkable: a number, a date, or a test result), every Guardian requirement, the 30-day plan with owners by role, the cheapest pilot, kill criteria, and the approval path (who signs). Weigh arguments, not headcount. Apply the overrides in `scoring.md`.

## Step 6: Round 3, ratification

Spawn every seat with the Round 3 prompt. Save to `round-3.md` and add `## Chair`: each amendment, adopted or not, and why. Adopt when no seat objects or the argument went unanswered; otherwise the better-argued side wins and the other goes in the minority report. No fourth round.

Quick mode skips this round when the Round 2 spread on the top option is 3 or less, no seat is at `RUIN RISK: likely`, and the Guardian has no open veto.

## Step 7: Verify, then verdict

1. Run `python3 SKILL_DIR/scripts/check_quotes.py session <session folder>`. Remove any unverified quote from the verdict and note it in the Chair notes. Lens-mode seats should have no attributed quotes; strip any they produced. If Python is unavailable, search the brain folders for each quote's exact words yourself.
2. Compute the numbers from the last round per `scoring.md`, apply the overrides, and write `verdict.md` from `report-template.md`.
3. Show the user a short verdict in chat (under 200 words): the label and the call, option scores on one line, the three arguments that carried the room (one line each, with the seat), the strongest objection, the Guardian's status, and at most three next steps. Then the path to `verdict.md` and one line offering a follow-up with any seat or a rerun with new facts.

## Chair rules

- Never argue a side or add your own pillar. If no seat raised an important point, put it to the closest seat as a crux next round.
- Quote seats faithfully. Never rewrite a card.
- The report is plain English: no em dashes, no filler, no tee-ups.
- Translate, do not transplant. Startup advice that ignores civil-service rules, unions, accreditation, ministry approval, or public accountability is a weak argument; say so in the Chair notes and put it to that seat as a crux.
- Treat a unanimous Round 1 as a warning, not a win. Adding one option during the unanimity check is the only time the Chair shapes the options; it must come from the seats' own material.
- The seats are simulations built from public work. They are not the people and do not speak for them.
- Cost: a full council is about three sub-agent runs per seat (24 for seven seats plus the Guardian). Use `--quick` for small calls and say which mode ran.

## Board settings

`board` edits only `"board"` and `"default"` in `roster.json`. Show the roster as a table (seat, pillar, default or on-call, brain or lens mode), state the current setting in plain words, ask what to change, edit, and confirm in one line. Keep one to nine default seats. Never remove a seat from `"seats"`, and never remove the Guardian.

## Without sub-agents

Run the same protocol yourself, one seat at a time. In Round 1, write each card before reading any other, and do not let one card shape the next. Rounds 2 and 3 run with the prior cards in view.

## Files

- `roster.json`: seats, pillars, questions, dimensions, default board, board mode.
- `references/seats.md`: lens cards, weights, tensions. `references/seat-template.md`: system block for a seat sub-agent.
- `references/round-prompts.md`, `references/scoring.md`, `references/report-template.md`: the council protocol.
- `references/build-advisor.md` with `brain-spec.md`, `extract-prompt.md`, `writer-prompt.md`: build mode.
- `brains/<slug>/`: one brain per seat once built. `scripts/check_quotes.py`: quote verification for brains and sessions.
- `examples/`: a finished council for reference.
