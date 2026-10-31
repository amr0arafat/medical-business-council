# Brains

One folder per seat, named by the seat's `slug` in `roster.json` (for example `andy-grove/`). Each holds the 8 files from `references/brain-spec.md`.

Seats without a brain run in **lens mode** (paraphrase from their lens card in `references/seats.md`, no quotes). Build a seat's brain with `build <name>` (see `references/build-advisor.md`) and that seat switches to **brain mode** automatically on the next council.

| Seat | Brain | Sources | Built |
|---|---|---|---|
| Grove | `andy-grove/` | 13 sources, ~69k words, 1987 to 2010, 309 verified quotes | 2026-10-31 |
| Hastings | `reed-hastings/` | 10 sources, ~48k words, 2014 to 2026, 294 verified quotes | 2026-10-31 |
| Musk | `elon-musk/` | 13 sources, ~48k words, 2003 to 2025, 304 verified quotes | 2026-10-31 |
| Bezos | `jeff-bezos/` | 9 sources, ~57k words, 1997 to 2023, 286 verified quotes | 2026-10-31 |
| Gates | `bill-gates/` | 9 sources, ~52k words, 2007 to 2023, 238 verified quotes | 2026-10-31 |
| Nadella | `satya-nadella/` | 11 sources, ~44k words, 2014 to 2025, 308 verified quotes | 2026-10-31 |

The whole default board now runs in brain mode. On-call seats (Jobs, Collison, Doerr, Horowitz, Huang) still run in lens mode until built.
