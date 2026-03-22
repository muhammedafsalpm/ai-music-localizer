import os
import subprocess

def separate_audio(path):
    # Demucs requires torchaudio which recently made torchcodec a hard dependency for saving files.
    # We dynamically install it here so the pipeline doesn't crash on this machine.
    try:
        import torchcodec
    except ImportError:
        print("Missing 'torchcodec'. Installing it now to fix the demucs crash...")
        subprocess.run(["pip", "install", "torchcodec"], check=True)

    subprocess.run(f"demucs --two-stems=vocals {path}", shell=True, check=True)

    base = "separated/htdemucs"
    folders = sorted(os.listdir(base), key=lambda x: os.path.getmtime(os.path.join(base, x)), reverse=True)
    folder = folders[0]

    return {
        "vocals": f"{base}/{folder}/vocals.wav",
        "instrumental": f"{base}/{folder}/no_vocals.wav"
    }