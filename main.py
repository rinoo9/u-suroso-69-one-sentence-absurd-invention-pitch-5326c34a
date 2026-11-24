"""One-Sentence Absurd Invention Pitch: a washing machine that confesses.

The entry is one sentence (163 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance: the washing machine that eats a sock
and, instead of leaving a mystery, texts you a photo of it with a caption.
The laugh comes from the machine itself -- a household appliance calmly
confessing to sock theft and reporting that the sock is happy now -- and
the fix is weirdly plausible: laundry losses stop being a mystery and
become closure. The program writes the entry deterministically to
/output/entry.txt (no trailing newline).

The 1-220 character gate and the single-sentence rule are enforced at
runtime (asserts below) so the entry can never drift past the limit on a
later edit.
"""

import os

ENTRY = (
    "My washing machine now texts me a photo of every sock it eats, "
    "captioned 'he's happy here now', so laundry day ends with closure "
    "instead of a missing-sock mystery."
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
