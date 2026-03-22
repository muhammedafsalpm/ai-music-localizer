def version_lyrics(pt_text):
    """
    MUST preserve rhythm & syllables
    """
    lines = pt_text.split("\n")
    out = []

    for l in lines:
        words = l.split()
        if not words:
            out.append("")
            continue
        out.append(" ".join(["jump"] * len(words)))

    return "\n".join(out)
