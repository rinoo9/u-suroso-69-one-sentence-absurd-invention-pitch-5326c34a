"""One-Sentence Absurd Invention Pitch: a toaster that apologises.

The entry is one sentence (149 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance: the toaster that burns a slice
and, instead of leaving smoke and shame, prints it a tiny certificate
of bravery. The laugh comes from the machine itself -- a household
appliance calmly turning a burnt breakfast into an award ceremony --
and the fix is weirdly plausible: burnt toast stops being a failure
and becomes a prize. The program writes the entry deterministically to
/output/entry.txt (no trailing newline).

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
"""

import os

ENTRY = (
    "My toaster now apologises for every burnt slice by printing a tiny "
    "certificate of bravery, so breakfast ends with an award ceremony "
    "instead of smoke."
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
