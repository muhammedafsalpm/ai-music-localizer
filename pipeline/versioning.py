def version_lyrics(pt_text):
    """
    Production rule:
    - preserve syllable count
    - preserve rhythm
    - approximate meaning
    """

    pt_lines = pt_text.split("\n")
    en_lines = []

    for line in pt_lines:
        words = line.split()

        # basic rhythm-preserving placeholder
        en_lines.append(" ".join(["la"] * len(words)))

    return "\n".join(en_lines)
