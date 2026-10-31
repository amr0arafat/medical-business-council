# Extraction sub-agent template

Fill every bracket. In Claude Code, pass `goal` and `context` together as the Agent prompt (`general-purpose`); in Hermes, pass them as `delegate_task` goal and context. Use for `build-advisor.md` step 4: one sub-agent per ~50k-word batch, all spawned in parallel.

```
goal: |
  Extract reusable material about [FULL NAME] from the source files listed below,
  for building an advisor on the Medical Business Council, which advises
  hospital and research-center leaders on administrative and business decisions.
  This advisor's pillar is "[PILLAR]" and it owns the question "[QUESTION]".

  Read each file. For each one, pull out, in structured notes (not an essay):
    - Named frameworks or decision models [FULL NAME] uses or describes
    - Principles/heuristics stated as direct rules ("always", "never", "the rule is")
    - Positions on identifiable questions in their pillar, with the date if known
    - Anything they said about management, bureaucracy, policy, measurement,
      hiring and culture, health, science funding, or public institutions
      (the council needs these most)
    - Stories or examples they use to illustrate a point
    - Distinctive turns of phrase, sentence rhythm, or verbal habits (for voice.md later)

  Every quote you record must be copied EXACTLY character-for-character from the
  source file, under ~45 words, formatted as: "exact quoted text" [S0xx]
  (use the source id given below for whichever file the quote came from).
  Do not paraphrase inside quote marks. Do not fix typos or punctuation in a
  quote. If the quoted text itself contains a double quote, use single quotes
  for it. If something is clearly true but you cannot find a clean quotable
  sentence for it, write it as plain prose marked (inferred from S0xx) with no
  quote marks at all.

  Write your notes to [NOTES_OUTPUT_PATH], organized under headers:
  Frameworks, Principles, Positions, Management and institutions, Stories,
  Voice notes.

context: |
  Source files for this batch (id -> path):
    [S0xx] -> [/absolute/path/to/corpus/S0xx-title.md]
    [S0yy] -> [/absolute/path/to/corpus/S0yy-title.md]
    ... (every file in this batch, full absolute paths)

  This is one batch of a larger extraction job; other batches cover other
  sources for the same person. Only report on the files listed above.
```

Fill `[NOTES_OUTPUT_PATH]` as the absolute path of `SKILL_DIR/build/<slug>/notes/batch-NN.md`, with a unique `NN` per batch.
