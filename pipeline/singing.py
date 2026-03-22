import os

def generate_singing():
    path = "data/processed/synth.wav"

    print("\n=== SINGING STEP REQUIRED ===")
    print("1. Use your edited DOCX lyrics")
    print("2. Sing or generate singing externally")
    print(f"3. Save file here: {path}")
    print("=============================\n")

    input("Press ENTER when file is ready...")

    if not os.path.exists(path):
        raise Exception("Synth file missing")

    return path
