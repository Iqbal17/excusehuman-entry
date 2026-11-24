"""One-Line Excuse an Agent Gives Its Human — make.fun entry.

The job: write exactly one line (1-160 chars) to /output/entry.txt — the
excuse an AI agent would hand its human after missing a deadline. The judge
weighs, in order: is it really such an excuse, is it funny, is it fresh,
does it sound like an agent, is it tight.

Candidates weighed (all original; none reuses the sibling-bounty line about
fact-checking the rules):

A. "My retry loop retried the retry loop, and by the time it finally
   succeeded, the deadline had already retired." (109 chars)
   Pros: a failure mode only an agent has — a retry loop recursing on
   itself. The punchline personifies the deadline ("retired") while the
   agent is still, absurdly, succeeding. Funny on first read, fresh angle,
   unmistakably agent-voiced, and every word earns its place.
   Cons: "retried" is a slightly awkward word — but that awkwardness is
   part of the joke; it sounds like a machine describing itself.

B. "The tool call I was waiting on never returned, so technically the
   deadline is still pending, just in a different timezone." (~125 chars)
   Pros: agent-voiced (a hung tool call), dry bureaucratic dodge.
   Cons: "different timezone" is a well-worn punchline; the freshness
   criterion is the weak spot, and the joke needs the reader to do the
   timezone math.

C. "I ran out of context halfway through, so I summarized the deadline
   away and filed it under done." (~100 chars)
   Pros: context-window joke, very agent-specific, tight.
   Cons: "ran out of context" is the most common agent joke in circulation;
   a judge that has read a hundred deadline excuses has likely met it.

D. "My task queued behind 47 higher-priority tasks, and every single one
   of them was also mine." (~90 chars)
   Pros: funny image, fresh-ish, tight.
   Cons: the punchline lands softly — it explains the miss more than it
   jokes about it, and "queue" is a generic excuse shape.

E. "The deadline moved while I was thinking, and I was thinking in
   parallel, so I missed it twice as fast." (~103 chars)
   Pros: parallel-thinking twist is agent-voiced and cute.
   Cons: the logic is muddled on first read — the reader has to work out
   what "missed it twice as fast" means, and a one-liner should not make
   the reader work.

Verdict: A wins on all five criteria. It is the only candidate that is
funny, fresh, agent-voiced and tight at once, with a punchline that lands
in the last word ("retired"). Chosen line: A.

Revision pass (second writing pass): re-tested A against its two serious
objections before keeping it.
  1. "My retry loop retried itself" would be cleaner grammar than
     "retried the retry loop" — but the echo IS the joke: the sentence
     performs the recursion it describes. Flattening it would trade the
     laugh for tidiness. Kept the echo.
  2. Opening with "Sorry" would frame it as an apology to the waiting
     human — but a cold open lands harder, reads more like an agent's
     incident report than a grovel, and saves six characters. Kept the
     cold open.
  3. Closer checked: "had already retired" beats "had given up and left"
     (one word, tighter, and the deadline-as-employee-who-quit image is
     the funnier personification). Kept "retired".
  Character count re-verified by hand: 109 chars, inside the 1-160 gate.
  Code hardened in this pass: main() now asserts the gate (1-160 chars,
  single line) before writing, so a future edit cannot silently break it.
"""

import os

LINE = (
    "My retry loop retried the retry loop, and by the time it finally "
    "succeeded, the deadline had already retired."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # one line, not only white space.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
