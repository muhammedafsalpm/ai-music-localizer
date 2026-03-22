import os

def run_voice_conversion(vocal_path):
    model = "models/rvc_model/giramille_voice.pth"

    if not os.path.exists(model):
        raise Exception("Model missing")

    print("Run RVC using:")
    print("Model:", model)
    print("Input:", vocal_path)

    input("Press ENTER after conversion...")

    return "data/processed/generated_vocals.wav"