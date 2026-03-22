import subprocess
from docx import Document

def clean_lyrics(text):
    lines = text.split("\n")
    clean = []

    for l in lines:
        l = l.strip()
        if len(l) < 3:
            continue
        clean.append(l)

    return "\n".join(clean)


def extract_lyrics(vocal_path):
    subprocess.run(
        f'whisper "{vocal_path}" --model large-v3 --language pt --output_format txt',
        shell=True,
        check=True
    )
    return "lyrics.txt"


def create_docx(text_path):
    doc = Document()
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    cleaned_text = clean_lyrics(text)
    doc.add_paragraph(cleaned_text)

    path = "lyrics/english_lyrics.docx"
    doc.save(path)
    return path