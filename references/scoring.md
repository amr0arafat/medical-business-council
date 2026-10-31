# Scoring

All numbers come from the seats' cards. The Chair computes, never invents. Use the last round that ran (Round 3 if it ran, else Round 2).

## Option scores

Every card scores every option 0 to 10. For each option:

`option score = sum(weight x seat score) / sum(weight)`, one decimal. The Guardian's scores count like any seat's.

Show each option's math on one line, for example: `B (3x7 + 3x6 + 2x8 + 2x5 + 2x7) / 12 = 6.6`.

The recommended option is the highest option score, unless an override removes it.

## Verdict bands (on the recommended option)

| Option score | Verdict |
|---|---|
| 7.5 to 10 | GO |
| 6.0 to 7.4 | GO WITH CONDITIONS |
| 4.5 to 5.9 | RESHAPE |
| below 4.5 | DON'T DO IT |

Three labels replace the band when they fit better, and the report says why:

- **PILOT FIRST**: the option is promising but rests on an untested assumption that a pilot in one department, unit, or process can check within 90 days. Names the pilot, its success metric, and the date it turns into GO or stops.
- **WAIT**: good, but blocked by a prerequisite outside the team's control (a ministry or board approval, a budget cycle, an accreditation visit, a hire). Names the trigger, the date, and what happens if it fails.
- **DON'T DO IT** also applies when "keep the current way" is itself the top score.

## Overrides (applied after the band, stated in the report)

1. **Guardian veto.** If the Guardian ends at `VETO: yes` on the recommended option, the verdict is capped at RESHAPE and the resolution must include the Guardian's named fix. If no fix is possible (the law forbids the option outright), that option gets DON'T DO IT and the next-best option is reported. The veto cannot be outvoted.
2. **Ruin cap.** Any seat at `RUIN RISK: likely` on the recommended option caps the verdict at RESHAPE until the resolution names a mitigation that seat endorsed.
3. **One-way door cap.** If the recommended option is a one-way door (Bezos's call, or a majority of seats) and the spread on it is 4 or more, cap at GO WITH CONDITIONS and make the cheapest pilot a precondition.
4. **Unanimity check.** If every seat's top option is the same and their scores sit within 1 point in Round 1, the Chair names the strongest unargued alternative as a crux in Round 2 and asks the seats whose pillars are most at risk to argue it at full strength. When that alternative is a distinct plan rather than a variant of an existing option, the Chair adds it as a new scored option (the next letter, D, E) under the rules in "Chair-added options" below.

## Chair-added options

The Chair may add one option, and only during the unanimity check. Adding options at other times turns the Chair into a seat.

- **Where it comes from.** It must come from the seats' own material: a point raised in a card, a condition several seats share, or the obvious variant the brief's options left out. The Chair never adds an option from its own pillar.
- **How it is written.** One plain paragraph in the Round 2 prompt and in `round-1.md` Chair notes: what it does, what it costs, and how it differs from the closest existing option. Label it "added by the Chair (unanimity check)".
- **Who argues it.** Assign it to at least two seats, preferably the highest-weight seats whose pillars it serves, to argue at full strength whatever they conclude. Assign at least one seat from the Round 1 majority to answer it directly.
- **Scoring.** Every seat scores it in Rounds 2 and 3 alongside A, B, C. It wins only on the same math as any option; the Chair's adding it carries no weight.
- **Guardian.** The Guardian gives a veto status on it like any option. If the Guardian vetoes it and no fix exists, it drops out.
- **Reporting.** The verdict says the option was Chair-added, why, and which seats were assigned to argue it. If it wins, the minority report names the least-tested assumption behind it.
- **Round 1 scores stand.** Seats did not score it in Round 1; do not backfill. The scorecard shows it from Round 2 on.

## Resolution support

Round 3's FINAL SCORE is each seat's support for the draft resolution as written. Report its weighted average as "Support for the resolution". It measures how well the Chair's plan captured the room, not whether the idea is good.

## Spread and confidence

- `spread` = highest minus lowest seat score on the recommended option.
- `council confidence` = average seat confidence x 2, rounded, minus 1 if the spread is 5 or more, minus 1 if half or more of the persona seats ran in lens mode. Scale 1 to 10.

## Pillar scorecard

One column per seat: its final PILLAR SCORE, labeled with its `dimension` from `roster.json`. Any pillar at 4 or below gets a named fix in the 30-day plan, even when the verdict is GO.
