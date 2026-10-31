#!/usr/bin/env python3
"""Verify that every attributed quote is real.

Two modes:

  brain    Notes or brain files against the raw corpus (build mode).
           Every "exact text" [S0xx] must appear in the corpus file for S0xx.
           python3 check_quotes.py brain <notes_or_brain_dir> <corpus_dir>

  session  A council session against the brains (after a council run).
           Every quote attributed to a source id, like "..." (S014) or
           "..." [S014], in round-*.md, draft-resolution.md, and verdict.md
           must appear in some brain, or in the brief or an earlier session
           file (a seat quoting another seat or the user).
           python3 check_quotes.py session <session_dir> [--brains <dir>]

Matching ignores case, whitespace, and curly versus straight quotes.
Session mode also ignores punctuation, since seats reformat lines slightly.
Exit code 0 if every quote verifies, 1 if any fail, 2 on usage errors.
"""
import re
import sys
from pathlib import Path

DEFAULT_BRAINS = Path(__file__).resolve().parents[1] / "brains"

BRAIN_QUOTE_RE = re.compile(r'"([^"\n]{10,}?)"\s*\[(S\d+)\]')
SESSION_QUOTE_RE = re.compile(r'"([^"\n]{20,400})"[^\n"]{0,40}?[\(\[](S\d{2,})')

CURLY = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-"})


def norm(text):
    return re.sub(r"\s+", " ", text.translate(CURLY)).strip().lower()


def loose(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' ]+", " ", norm(text))).strip()


def straighten(text):
    return text.translate(CURLY)


def usage(msg=None):
    if msg:
        print(f"ERROR: {msg}")
    print(__doc__)
    sys.exit(2)


def find_corpus_file(corpus_dir, source_id):
    matches = sorted(corpus_dir.glob(f"{source_id}-*")) + sorted(corpus_dir.glob(f"{source_id}.*"))
    return matches[0] if matches else None


def check_brain(notes_dir, corpus_dir):
    md_files = sorted(notes_dir.glob("*.md"))
    if not md_files:
        usage(f"no .md files in {notes_dir}")

    cache, failures, total = {}, [], 0
    for md_file in md_files:
        for quote, source_id in BRAIN_QUOTE_RE.findall(straighten(md_file.read_text(errors="replace"))):
            total += 1
            if source_id not in cache:
                cfile = find_corpus_file(corpus_dir, source_id)
                cache[source_id] = norm(cfile.read_text(errors="replace")) if cfile else None
            if cache[source_id] is None:
                failures.append((md_file.name, source_id, quote, "source file not found"))
            elif norm(quote) not in cache[source_id]:
                failures.append((md_file.name, source_id, quote, "not found verbatim in that source"))

    print(f"Checked {total} quotes across {len(md_files)} file(s): {total - len(failures)} ok, {len(failures)} failed.")
    for fname, sid, quote, reason in failures:
        snippet = quote if len(quote) <= 80 else quote[:77] + "..."
        print(f"  [{sid}] in {fname}: {reason}\n      \"{snippet}\"")
    return 1 if failures else 0


def check_session(session_dir, brains_dir):
    brain_files = list(brains_dir.rglob("*.md")) if brains_dir.exists() else []
    brain_text = loose(" ".join(p.read_text(errors="replace") for p in brain_files))

    brief = session_dir / "brief.md"
    seen = loose(brief.read_text(errors="replace")) if brief.exists() else ""
    files = sorted(session_dir.glob("round-*.md")) + [
        p for p in (session_dir / "draft-resolution.md", session_dir / "verdict.md") if p.exists()
    ]
    if not files:
        usage(f"no round-*.md or verdict.md in {session_dir}")

    ok, internal, bad = 0, 0, []
    for f in files:
        text = f.read_text(errors="replace")
        for quote, source_id in SESSION_QUOTE_RE.findall(straighten(text)):
            q = loose(quote)
            if len(q.split()) < 6:
                continue
            if brain_text and q in brain_text:
                ok += 1
            elif q in seen:
                internal += 1
            else:
                bad.append((f.name, source_id, quote))
        seen += " " + loose(text)

    print(f"Brain quotes verified: {ok}; quotes of the brief or earlier rounds: {internal}; unverified: {len(bad)}")
    if not brain_files:
        print("  (no brains found: every seat ran in lens mode, so any attributed quote is unverified)")
    for name, sid, quote in bad:
        print(f"  UNVERIFIED [{name}] ({sid}) \"{quote[:160]}\"")
    return 1 if bad else 0


def main():
    args = sys.argv[1:]
    if not args:
        usage()
    mode = args[0]

    if mode == "brain" and len(args) == 3:
        notes_dir, corpus_dir = Path(args[1]).expanduser(), Path(args[2]).expanduser()
        for d in (notes_dir, corpus_dir):
            if not d.is_dir():
                usage(f"directory not found: {d}")
        sys.exit(check_brain(notes_dir, corpus_dir))

    if mode == "session" and len(args) in (2, 4):
        session_dir = Path(args[1]).expanduser()
        brains_dir = DEFAULT_BRAINS
        if len(args) == 4:
            if args[2] != "--brains":
                usage()
            brains_dir = Path(args[3]).expanduser()
        if not session_dir.is_dir():
            usage(f"directory not found: {session_dir}")
        sys.exit(check_session(session_dir, brains_dir))

    usage()


if __name__ == "__main__":
    main()
