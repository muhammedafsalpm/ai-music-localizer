import os

def align_and_mix(vocals, instrumental):
    output = "data/output/final.wav"

    os.system(
        f'ffmpeg -i "{instrumental}" -i "{vocals}" '
        f'-filter_complex "[1:a]adelay=0|0[a1];[0:a][a1]amix=inputs=2:duration=longest" '
        f'"{output}"'
    )

    return output