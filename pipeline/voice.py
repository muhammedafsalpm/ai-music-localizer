import os

def run_voice_conversion(vocal_path):
    model_path = "models/rvc_model/giramille_voice.pth"

    if not os.path.exists(model_path):
        raise Exception("RVC model not found!")

    print("⚠️ Run RVC manually using this model:")
    print(model_path)
    print("Input:", vocal_path)

    input("After generating output, press ENTER...")

    return "data/processed/generated_vocals.wav"