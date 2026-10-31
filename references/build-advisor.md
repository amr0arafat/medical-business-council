# Build mode: give a seat an evidence-grounded brain

`build <name>` turns a seat from lens mode into brain mode, or adds a new advisor to the council. It compiles a text-only brain from the person's own public work (essays, letters, long talks, long interviews), and every quote in it is checked against the raw source text before it ships. Ported from roast-room's `newroaster` skill, without the portrait pipeline.

## When to use

- "build the Grove brain", "upgrade Hastings to brain mode", "add Marc Benioff to the council"
- Don't use for fictional characters, private individuals, or anyone with too thin a public record (under ~15 usable sources / 60k words). Say so and offer `quick` depth, or decline.

## Paths

- Brain (keep): `SKILL_DIR/brains/<slug>/{sources,frameworks,principles,positions,stories,voice,books,_hot}.md`
- Build scratch (disposable): `SKILL_DIR/build/<slug>/{urls.txt,corpus/S001-<title>.md,sources.json,notes/batch-NN.md}`
- Quote format in every notes and brain file: `"exact quoted text" [S003]` (straight quotes, bracketed id right after)

Tool names below use Claude Code first, Hermes second (see the table in SKILL.md).

## Procedure

1. **Define the seat.** Full name, the pillar and the one question this advisor owns **for healthcare administration**, and depth: `quick` (12-20 sources, 80k+ words, 2-3 extractors), `standard` (30-50 sources, 250k+ words, 4-6 extractors), `deep` (80+ sources, 500k+ words, 8-12 extractors in waves). Ask only what is missing, in one batch. Derive `slug` (first-last, lowercase-hyphen) and `key` (usually the surname). If the key is already in `roster.json`, this is an upgrade: keep its pillar and question unless the user asks to change them.

2. **Find sources** (WebSearch / `web_search`). The person's own essays, letters, blog, long keynotes where they are the main speaker, long interviews, and material from the last two years so positions are current. Prefer anything where they talk about management, organizations, health, science, or public institutions, since that is what the council will ask. Skip clips under ~10 minutes, compilations, and pieces where someone else does most of the talking. One URL per line in `build/<slug>/urls.txt`. Aim for the depth target plus ~20%, since some fetches fail.

3. **Fetch** (WebFetch / `web_extract`, up to 5 per batch). Save each as `corpus/S001-<title>.md`, `S002-...`, and log `{id, url, title, date, word_count}` in `sources.json`. Replace anything paywalled, empty, or off-topic. Stop when the depth target is met. Spot-check 2-3 corpus files: clean text, on topic, actually by this person.

4. **Extract (map).** Split sources into ~50k-word batches. Spawn one sub-agent per batch, **all in one message/call** (cap ~6 at once; `deep` runs in waves), with `extract-prompt.md` filled in. Each writes `notes/batch-NN.md`. Wait for all of them.

5. **Verify quotes (pre-check).** `python3 SKILL_DIR/scripts/check_quotes.py brain SKILL_DIR/build/<slug>/notes SKILL_DIR/build/<slug>/corpus`. Fix what it flags in the notes: wrong id, correct it; quote not found, delete it or rewrite it as plain prose marked `(inferred from S0xx)` with no quote marks.

6. **Write the brain (reduce).** Spawn 3 writers in one message with `writer-prompt.md`: Writer A, `frameworks.md` `principles.md` `books.md`; Writer B, `positions.md` `stories.md`; Writer C, `voice.md`. They follow `brain-spec.md`. Then you write `sources.md` from `sources.json`, and `_hot.md` yourself (under 800 words, including the "healthcare translation" section from `brain-spec.md`).

7. **Verify quotes (final).** Re-run the checker on `brains/<slug>` against `build/<slug>/corpus`. Fix until clean.

8. **Register.** For a new advisor, add one entry to `roster.json` `"seats"` (`key, name, short, slug, kind: "persona", pillar, question, dimension`), add a lens card to `seats.md` (same shape as the others), and add one or two tension lines. Do not add them to `"default"` unless the user asks.

9. **Test the seat.** Spawn one sub-agent with the single-seat consult prompt from `round-prompts.md` and a sample admin question in their pillar (for example "Should our university hospital cut the purchase approval chain from seven signatures to three?"). Check: sounds like `voice.md`, cites source ids, every quote passes the checker, respects healthcare constraints, and says plainly it is a simulation if asked.

10. **Report** (under 150 words): who, pillar and question, source and word counts and years covered, where the brain lives, and that the seat now runs in brain mode.

## Pitfalls

- A sub-agent starts with zero memory of this conversation. Extract and writer prompts must be self-contained (name, pillar, absolute file paths, exact quote format) or quality drops silently.
- Never paste a 250k-word corpus into a prompt. Give file paths and let the sub-agent read them.
- A thin corpus produces an advisor that paraphrases generically. Tell the user instead of shipping a weak seat.
- The checker confirms a quote appears in the file of the cited source id, so a wrong id fails. It normalizes case, whitespace, and curly quotes only; it does not judge whether the quote is used in context. Spot-check a handful by hand.
- `build/` is disposable and large; only `brains/` is worth keeping. Never copy book prose into a brain (copyright); use how the person teaches the ideas in public.
- Most of these leaders never spoke about hospital administration. The brain records what they said; the healthcare translation in `_hot.md` is marked as inference, never as their words.

## Done when

- `brains/<slug>/` has all 8 files, each non-empty.
- The checker reports zero unverified quotes on `brains/<slug>`.
- The test consult reads in voice, cites ids, respects healthcare constraints, and gives the simulation disclaimer when asked.
- `roster.json` has exactly one entry for the key.
