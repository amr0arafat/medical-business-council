# Brain-writer sub-agent template

Fill every bracket. In Claude Code, pass `goal` and `context` together as the Agent prompt (`general-purpose`); in Hermes, pass them as `delegate_task` goal and context. Use for `build-advisor.md` step 6: three writers, spawned in parallel, each owning different output files.

```
goal: |
  Write [OUTPUT FILES, e.g. "frameworks.md, principles.md, and books.md"] for an
  advisor persona brain modeling [FULL NAME] (pillar: "[PILLAR]", core question:
  "[QUESTION]").

  This advisor sits on the Medical Business Council, which advises hospital and
  research-center leaders on administrative and business decisions. Where the
  notes include material on management, bureaucracy, policy, measurement,
  culture, health, science, or public institutions, give it priority.

  Read every notes file listed in context. Combine and de-duplicate their
  content into your assigned output file(s), following the per-file rules in
  the brain spec (pasted below in context). Keep every quote EXACTLY as it
  appears in the notes, in the format "exact text" [S0xx]. Do not alter, trim,
  or re-word a quote. If two notes files quote the same thing, keep it once.
  Do not invent anything the notes do not support.

  Write each output file to:
    [ABSOLUTE PATH OF SKILL_DIR/brains/<slug>/<file>.md]

  Only write your assigned file(s). Do not touch any other file in that directory.

context: |
  Brain spec (per-file rules and word budgets):
  [PASTE THE RELEVANT sections of references/brain-spec.md HERE]

  Notes files to read (all batches, full text relevant to every writer):
    [/absolute/path/to/build/notes/batch-01.md]
    [/absolute/path/to/build/notes/batch-02.md]
    ... (every notes file from step 4)
```

Notes paths live in `SKILL_DIR/build/<slug>/notes/`. Always pass absolute paths.

Assignment used by this skill: Writer A -> frameworks.md, principles.md, books.md. Writer B -> positions.md, stories.md. Writer C -> voice.md.
