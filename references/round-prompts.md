# Round prompts

Each seat's prompt = the seat system block (`seat-template.md`) + one of the round prompts below. Replace the bracketed parts and give absolute paths. Seats read the brief and earlier rounds from the session folder, so cards stay verbatim without being pasted into every prompt.

Sub-agent type: `general-purpose` in Claude Code (`delegate_task` in Hermes). Spawn all seats of a round in one message or call.

**Options.** Every card scores every option in the brief (A, B, C, including "keep the current way"). For a single yes/no decision the options are "do it as proposed" and "don't". If the unanimity check added an option (`scoring.md`, "Chair-added options"), Rounds 2 and 3 score it too: add it to every OPTION SCORES line and to the Guardian's VETO lines.

**Pillar score.** The seat's score of the option it recommends, judged on its own pillar alone.

---

## Round 1: opening position

```
MEDICAL BUSINESS COUNCIL, ROUND 1 OF 3: OPENING POSITION

Read the brief: [absolute session folder]/brief.md

Your weight on this decision: [w]/3 ([one-line reason]).

Answer in your seat's voice, plain text, under 350 words, in exactly this shape:

SEAT: [SHORT] ([pillar])
STANCE: Strong yes | Yes | Conditional yes | No | Strong no   (on the option you recommend)
OPTION SCORES: [A] n/10 · [B] n/10 · [C] n/10
PILLAR SCORE: n/10   ([dimension]: the option you recommend, on your pillar alone)
CONFIDENCE: n/5
RUIN RISK: none | possible | likely   (an irreversible harm to the institution, its staff, its finances, its license, or its reputation, for the option you recommend)
DOOR: one-way | two-way
[GUARDIAN ONLY] VETO: no | yes, because [rule or standard], cleared by [exact fix]

THE CALL: one sentence, naming the option or a variant.
WHY:
1. argument, naming the framework you used and its source (brain mode: source id; lens mode: book, letter, or talk)
2. ...
3. ...
HEALTHCARE REALITY CHECK: one line on how this survives the brief's constraints (approvals, law, unions, audit, accreditation).
THE RISK I SEE: the single biggest thing that goes wrong.
WHAT WOULD CHANGE MY MIND: a concrete fact or number.
WHAT I'D DO IN THE NEXT 30 DAYS: one action, with the role that owns it.
QUESTION FOR THE DECISION-MAKER: the one question you would ask before signing off.

Rules: argue from your pillar first. Use the brief's numbers; say which you are assuming. Do not hedge.
```

---

## Round 2: debate

```
MEDICAL BUSINESS COUNCIL, ROUND 2 OF 3: DEBATE

Read: [absolute session folder]/brief.md and [absolute session folder]/round-1.md (every seat's card and the Chair's cruxes).

[ONLY IF THE UNANIMITY CHECK ADDED AN OPTION:]
NEW OPTION ADDED BY THE CHAIR (unanimity check):
D. [one plain paragraph: what it does, what it costs, how it differs from the closest option]. Score D alongside the others.
YOUR ASSIGNMENT: [argue D at full strength, whatever you conclude | answer the case for D directly | none]

THE CRUXES THE CHAIR SEES
1. [crux]: [seats on each side]. [If this seat is on one side, the argument it must answer.]
2. ...

Answer in your seat's voice, plain text, under 300 words, in exactly this shape:

SEAT: [SHORT]
I DISAGREE MOST WITH: [seat]. Their argument in one line, then your rebuttal.
I CONCEDE: the strongest point made against you and what it changes. "Nothing" only if you can say why it fails.
ON THE CRUXES: one or two lines each.
STANCE: ...
OPTION SCORES: [A] n/10 · [B] n/10 · [C] n/10
PILLAR SCORE: n/10
CONFIDENCE: n/5
RUIN RISK: none | possible | likely
[GUARDIAN ONLY] VETO: no | yes, because ..., cleared by ...
MOVED: no | yes, from X to Y, because ...
MY CONDITIONS FOR YES: up to three, checkable (a number, a date, a test result, an approval obtained).

Rules: engage the actual arguments. Move only for a better argument, never to be agreeable. If everyone agrees with you, find the weakest part of your own case and say it.
```

---

## Round 3: ratification

```
MEDICAL BUSINESS COUNCIL, ROUND 3 OF 3: VOTE ON THE DRAFT RESOLUTION

Read: [absolute session folder]/brief.md, your own section of [absolute session folder]/round-2.md, and [absolute session folder]/draft-resolution.md.

Answer in your seat's voice, under 150 words, in exactly this shape:

SEAT: [SHORT]
VOTE: Endorse | Endorse with amendment | Dissent
OPTION SCORES: [A] n/10 · [B] n/10 · [C] n/10   (given the resolution's conditions)
FINAL SCORE: n/10   (your support for the draft resolution as written)
FINAL PILLAR SCORE: n/10
[GUARDIAN ONLY] VETO: no | yes, because ..., cleared by ...
AMENDMENT OR DISSENT: one or two sentences. Blank if you endorse.
ONE LINE FOR THE DECISION-MAKER: the thing from your pillar they must not forget.
```

---

## Single-seat consult

```
MEDICAL BUSINESS COUNCIL, SINGLE-SEAT CONSULT

THE QUESTION
[question, plus any context about the institution]

Answer in your seat's voice, first person, under 500 words: your call, your reasoning with named frameworks and their sources, the healthcare reality check, what you would do in the next 30 days, and the question you would ask back. Brain mode: end with "Sources:" and the source ids you used. Lens mode: end with "Lens mode: paraphrased from public work, no verified quotes."
```
