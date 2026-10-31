# Brain Spec

A brain is 8 markdown files in `SKILL_DIR/brains/<slug>/`. Every quote anywhere in the brain uses the format `"exact text" [S0xx]` (straight double quotes, bracketed id immediately after) so `scripts/check_quotes.py` can find and verify it. A line with no verifiable quote is plain prose marked `(inferred from S0xx)`. Never put inference inside quote marks.

The brain records what the person said in public, about anything. The council applies it to hospital and research-center administration, so writers should give extra room to what the person said about management, organizations, policy, measurement, health, science, and public institutions.

## sources.md
One line per source: `- [S0xx] Title, URL (YYYY-MM-DD, ~N words)`. Generated from `build/sources.json`, not hand-written.

## frameworks.md (~1500-2500 words)
Named, reusable mental models or decision frameworks the person actually uses and names. For each: the name they give it (or a short label if they never named it), 2-4 sentences explaining it in their terms, and at least one verbatim quote. Skip anything you can't tie to a source id.

## principles.md (~800-1500 words)
Short, repeatable heuristics/rules the person states directly ("always...", "never...", "the rule is..."). One line each: the principle, then its quote and id. These are terser and more quotable than frameworks.

## positions.md (~1000-2000 words)
Where the person stands on specific, identifiable questions in their pillar -- especially recent ones (last 2 years), so views-over-time are visible. Note the date of each position and flag any documented change of mind ("said X in 2019, revised to Y by 2023 [S0xx]/[S0yy]").

## stories.md (~800-1500 words)
Anecdotes or examples the person tells more than once, or one vivid illustrative story per major point. These are what make the persona sound like a person instead of a position paper -- keep them close to verbatim, tagged with source ids.

## voice.md (~500-1000 words)
How they actually talk: sentence length and rhythm, recurring phrases or verbal tics, what they'd never say, formality level, how they handle disagreement. Write this as direct guidance to whoever will roleplay them ("keeps sentences under 15 words", "never swears", "answers a hard question with a story first"), each claim backed by a quote where possible.

## books.md (~400-800 words)
Books they wrote or reference often -- never reproduce book text itself (copyright). Use only how the person themselves describes/teaches the ideas in interviews, talks, or their own essays, each claim quoted or cited to a source id.

## _hot.md (strictly under 800 words)
Written by the orchestrator (not a subagent), after all 6 files above exist. This is the fast-load summary for consult time, in four sections:

1. **Questions they ask**: 5-6 questions this person asks of any decision in their pillar.
2. **Sharpest heuristics**: their 2-3 sharpest rules, each with its source id.
3. **Healthcare translation**: 3-5 lines on how the lens applies to a hospital or research center (approval chains, public budgets, unions, accreditation, researchers' time). Every line marked `(inferred)`, because the person rarely said it about hospitals.
4. **Where this lens misfires**: the honest limits of thinking their way, especially in regulated, public, or safety-critical settings.

No new quotes here. Synthesize from the other files.

## Rules
- Every quote under ~45 words, copied exactly, never paraphrased inside quote marks.
- Never reproduce full paragraphs of copyrighted book text. Quotes from interviews or talks about the book are fine; the book's own prose is not.
- A claim with no quotable source is plain prose marked `(inferred from S0xx)`, not dressed up as a quote.
- Use straight double quotes only inside quotes; never put a `"` character inside a quoted string (the checker stops at it). Use single quotes for a quote within a quote.
- Plain, short sentences in anything you write yourself (sources.md, _hot.md). No filler, no em dashes.
