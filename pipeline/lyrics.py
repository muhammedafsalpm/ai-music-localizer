import subprocess
from docx import Document

def extract_lyrics(vocal_path):
    subprocess.run(
        f'whisper "{vocal_path}" --model large-v3 --language pt --output_format txt',
        shell=True,
        check=True
    )
    return "lyrics.txt"


def create_docx(text_path):
    doc = Document()
    with open(text_path, "r") as f:
        doc.add_paragraph(f.read())

    path = "lyrics/english_lyrics.docx"
    doc.save(path)
    return path