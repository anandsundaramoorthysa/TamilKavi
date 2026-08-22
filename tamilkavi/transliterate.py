"""Romanise Tamil so it can be read in a terminal.

No terminal renders Tamil script correctly. The grid gives one cell per code
point, but a Tamil letter is usually several code points that have to be
composed into a single shape, so clusters break apart wherever they are drawn.
That is true of every terminal on every operating system, and no package can
change it.

Latin, on the other hand, renders perfectly everywhere. So rather than draw
Tamil badly, we write the same poem in the alphabet the terminal can handle --
the Tanglish that Tamil speakers already use to text each other.

This is deliberately readable rather than reversible. It is meant for someone
to read aloud, not to be converted back into Tamil. Use --read for the real
script.
"""

# Independent vowels. Long vowels are written the way people actually type them
# rather than by a strict doubling rule, because this exists to be read.
UYIR = {
    "அ": "a",  "ஆ": "aa", "இ": "i",  "ஈ": "ee",
    "உ": "u",  "ஊ": "oo", "எ": "e",  "ஏ": "ae",
    "ஐ": "ai", "ஒ": "o",  "ஓ": "o",  "ஔ": "au",
}

# Vowel signs, in the same scheme. "" is the inherent 'a' of a bare consonant.
SIGNS = {
    "":  "a",   "ா": "aa", "ி": "i",  "ீ": "ee",
    "ு": "u",   "ூ": "oo", "ெ": "e",  "ே": "ae",
    "ை": "ai",  "ொ": "o",  "ோ": "o",  "ௌ": "au",
}

# Consonants at the start of a word, doubled, or after another consonant.
MEI = {
    "க": "k",  "ங": "ng", "ச": "s",  "ஞ": "nj", "ட": "t",  "ண": "n",
    "த": "th", "ந": "n",  "ப": "p",  "ம": "m",  "ய": "y",  "ர": "r",
    "ல": "l",  "வ": "v",  "ழ": "zh", "ள": "l",  "ற": "r",  "ன": "n",
    "ஜ": "j",  "ஷ": "sh", "ஸ": "s",  "ஹ": "h",
}

# Tamil has no separate voiced letters: the same consonant softens when it sits
# between vowels. நதி is "nathi", but அதிபதி is "adhipathi". Applying this is
# what makes the output read like Tamil instead of a letter-by-letter code.
VOICED = {"க": "g", "ச": "s", "ட": "d", "த": "dh", "ப": "b"}

# After one of these nasals a stop is voiced too, which is why பொங்கல் is
# "pongal" and இன்பம் is "inbam".
NASALS = {"ங", "ஞ", "ண", "ந", "ம", "ன"}

PULLI = "்"
AYTHAM = "ஃ"


def _split(word):
    """Split a Tamil word into (consonant, vowel_sign) pairs and bare vowels.

    Yields tuples of (kind, base, sign) where kind is 'uyir', 'mei' (consonant
    with no vowel) or 'uyirmei' (consonant carrying a vowel).
    """
    i = 0
    while i < len(word):
        ch = word[i]
        if ch in UYIR:
            yield ("uyir", ch, "")
            i += 1
        elif ch in MEI:
            nxt = word[i + 1] if i + 1 < len(word) else ""
            if nxt == PULLI:
                yield ("mei", ch, "")
                i += 2
            elif nxt in SIGNS and nxt:
                yield ("uyirmei", ch, nxt)
                i += 2
            else:
                yield ("uyirmei", ch, "")
                i += 1
        elif ch == AYTHAM:
            yield ("uyir", ch, "")
            i += 1
        else:
            yield ("other", ch, "")
            i += 1


def romanise_word(word):
    """Romanise a single Tamil word."""
    units = list(_split(word))
    out = []

    for index, (kind, base, sign) in enumerate(units):
        if kind == "other":
            out.append(base)
            continue
        if base == AYTHAM:
            out.append("h")
            continue
        if kind == "uyir":
            out.append(UYIR[base])
            continue

        previous = units[index - 1] if index else None
        following = units[index + 1] if index + 1 < len(units) else None
        letter = MEI[base]

        if kind == "mei":
            if following is not None and following[1] == base and len(letter) > 1:
                # A doubled consonant written as a digraph comes out unreadable
                # -- த்த would be "ththa". Drop this half and let the next one
                # carry the sound, giving "paartha" and "vaazhthu".
                letter = ""
            elif base == "ங" and following is not None and following[1] == "க":
                # ங் + க is a single "ng" sound: பொங்கல் is "pongal", not
                # "ponggal". The க that follows supplies the g.
                letter = "n"
            out.append(letter)
            continue

        # A stop softens between vowels, and also after a nasal: நதி is
        # "nathi" but அதிபதி is "adhipathi", and பொங்கல் is "pongal".
        # It stays hard when doubled (ட்ட is "tt", never "td").
        doubled = previous is not None and previous[0] == "mei" and previous[1] == base
        after_vowel = previous is not None and previous[0] in ("uyir", "uyirmei")
        after_nasal = previous is not None and previous[0] == "mei" and previous[1] in NASALS

        if base in VOICED and not doubled and (after_vowel or after_nasal):
            letter = VOICED[base]

        out.append(letter + SIGNS.get(sign, ""))

    return "".join(out)


def romanise(text):
    """Romanise Tamil text, preserving line breaks, spacing and punctuation."""
    if not text:
        return text

    out = []
    buffer = []
    for ch in str(text):
        if ch in UYIR or ch in MEI or ch in SIGNS or ch == PULLI or ch == AYTHAM:
            buffer.append(ch)
        else:
            if buffer:
                out.append(romanise_word("".join(buffer)))
                buffer = []
            out.append(ch)
    if buffer:
        out.append(romanise_word("".join(buffer)))

    result = "".join(out)
    # Capitalise the first letter of each line so it reads like written verse.
    return "\n".join(
        line[:1].upper() + line[1:] if line[:1].isalpha() else line
        for line in result.split("\n")
    )


def has_tamil(text):
    """True if the text contains any Tamil script."""
    return any("஀" <= ch <= "௿" for ch in str(text or ""))
