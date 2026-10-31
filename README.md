# Medical Business Council

A council of Silicon Valley operators, plus a Governance Guardian with veto power, that debates **non-clinical** administrative and business decisions for hospitals, clinics, medical faculties, and research centers. You bring the decision; the seats argue it over three rounds; the Chair returns a scored verdict, the dissent, the compliance requirements, and a 30-day plan.

It is an agent skill for [Claude Code](https://claude.com/claude-code) and Hermes Agent, inspired by [roast-room](https://github.com/nateherkai/roast-room).

> The seats are simulations built from public words. They are not the people and do not speak for them. Verdicts are decision support, not legal, financial, or clinical advice. See [NOTICE.md](NOTICE.md).

## The board

| Seat | Owns the question | Brain |
|---|---|---|
| Bezos | Is this the right bet, and how reversible is it? | 9 sources, 1997 to 2023 |
| Grove | What is the output, where is the bottleneck, and who is measured on it? | 13 sources, 1987 to 2010 |
| Hastings | Does this policy add rules where talent and context would do better? | 10 sources, 2014 to 2026 |
| Nadella | Will people actually adopt this, and does it make the institution a learn-it-all? | 11 sources, 2014 to 2025 |
| Musk | Which requirement is real, which step can be deleted, and what is the true constraint? | 13 sources, 2003 to 2025 |
| Gates | What does it cost, what measurable result does it buy, and is the funding sustainable? | 9 sources, 2007 to 2023 |
| **Governance Guardian** | Is it lawful, accreditable, fair to staff, and safe for patient data? Holds the only veto. | Role seat |

On call (summary cards only until you build their brains): Jobs, Collison, Doerr, Horowitz, Huang.

## What it is for

In scope: admin policy and SOPs, approval chains, staffing and incentives, scheduling and capacity as a business process, procurement and outsourcing, budgets and revenue lines, grants offices and research administration, digital and AI adoption, partnerships and strategy.

Out of scope: diagnosis, treatment, a specific patient, clinical protocols, or study design.

## Install

**Claude Code.** Copy this folder into your skills directory:

```bash
git clone https://github.com/amr0arafat/medical-business-council ~/.claude/skills/medical-business-council
```

or into a project at `.claude/skills/medical-business-council/`. Start a new session so the skill loads.

**Hermes Agent.** Place the folder in your Hermes skills directory. `SKILL.md` lists the Hermes tool names (`delegate_task`, `clarify`, `execute_code`) alongside the Claude Code ones.

Requirements: Python 3 for `scripts/check_quotes.py` (standard library only).

## Use

```
/medical-business-council Should our university hospital cut the purchase approval chain from seven signatures to three? 1,200 beds, public, Egypt. Median approval 34 days. I lean toward cutting it hospital-wide now.
```

Modes:

- `--quick`: three seats plus the Guardian, two rounds. For reversible calls.
- `--seats grove,hastings`: only the seats you name (the Guardian always sits).
- `--all`: every seat, up to nine.
- `ask grove <question>`: one seat, one answer.
- `board`: show or change the default board.
- `build <name>`: build an evidence-grounded brain for a seat or a new advisor.

Give the council the decision, two or three options (including "keep the current way"), your numbers, your limits (budget, approvals, law), what success looks like, and which way you lean. The council tests your lean instead of agreeing with it.

Each run writes `council-sessions/<date>-<decision>/` in your working folder: the brief, every round's cards, the draft resolution, and `verdict.md`. A full council is about 21 sub-agent runs; `--quick` is about 8.

## How it works

1. **Brief.** The Chair builds a brief, asks only for missing facts, and weights each seat 1 to 3 by how much the decision lives in its pillar.
2. **Round 1.** Every seat writes an opening card in parallel: stance, scores for each option, ruin risk, reversibility, and (for the Guardian) a veto line per option.
3. **Unanimity check.** A unanimous Round 1 is a warning. The Chair may add one option from the seats' own material and assign seats to argue it at full strength.
4. **Round 2.** Seats debate the cruxes, concede, and move only for better arguments.
5. **Draft resolution, Round 3.** Seats vote: endorse, amend, or dissent.
6. **Verdict.** Weighted scores, overrides (Guardian veto, ruin cap, one-way-door cap), conditions, a 30-day plan, approval path, and kill criteria. Every attributed quote is checked against the brains.

Details: [SKILL.md](SKILL.md), [references/scoring.md](references/scoring.md), [references/round-prompts.md](references/round-prompts.md).

## Brains

Each persona seat reads a brain in `brains/<slug>/`: frameworks, principles, dated positions, stories, voice, books, sources, and a short `_hot.md` with a healthcare translation and the honest limits of the lens. Every quote is verbatim from the person's own public words and carries a source id; `scripts/check_quotes.py` verifies each one against the source text before a brain ships.

Build or refresh one with `build <name>` ([references/build-advisor.md](references/build-advisor.md)). The raw downloads go to `build/`, which is git-ignored and should never be published.

## Example

[examples/2026-10-31-example-procurement-approvals/](examples/2026-10-31-example-procurement-approvals/) shows a finished brief and verdict for a fictional public hospital.

## Credits and license

MIT, see [LICENSE](LICENSE). The council protocol, scoring approach, and brain-building pipeline are adapted from [roast-room](https://github.com/nateherkai/roast-room) (MIT, AI Automation Society). Quotations in `brains/` belong to their authors and publishers; see [NOTICE.md](NOTICE.md).
