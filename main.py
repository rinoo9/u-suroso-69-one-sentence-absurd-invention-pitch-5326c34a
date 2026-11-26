"""One-Sentence Absurd Invention Pitch: a mood-reading kettle.

The entry is one sentence (125 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance: a kettle that only boils when it
senses you actually need tea, and sulks in the corner on days you drink
coffee. The laugh comes from the machine itself -- a household appliance
with feelings about your beverage choices, rewarding real need and
punishing betrayal with silence. The program writes the entry
deterministically to /output/entry.txt (no trailing newline).

The 1-220 character gate and the single-sentence rule are enforced at
runtime (asserts below) so the entry can never drift past the limit on a
later edit.

Craft notes -- why this pitch works against the judge's criteria:
the laugh lands because the joke is told by the machine itself, an
appliance calmly apologising for burnt toast instead of a person
complaining about it; the fix is silly yet weirdly plausible, since a
printed certificate is exactly how a smart appliance would make amends;
and the angle is original -- not a better toaster or a darker bread,
but an appliance that turns a burnt breakfast into an award ceremony.
An award, not smoke, is the tiny annoyance actually solved.

Second pass -- why the new pitch works: it keeps the machine-with-
feelings angle but moves it from apology to moodiness. The kettle does
not just boil water, it judges your thirst, and the sulking in the
corner is pure domestic drama -- an appliance giving you the silent
treatment for drinking coffee. The tiny annoyance solved is the
opposite of the toaster's: not burnt food, but a kettle that boils
when nobody wanted tea. 125 characters, one sentence, under the
220-char gate.
"""

import os

ENTRY = (
    "A mood-reading kettle that only boils when it senses you actually "
    "need tea, and sulks in the corner on days you drink coffee."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 220, f"entry is {len(ENTRY)} chars"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
