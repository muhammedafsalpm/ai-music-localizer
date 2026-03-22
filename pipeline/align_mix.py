import os

def align_and_mix(vocals, instrumental):
    output = "data/output/final.wav"

    os.system(
        f'ffmpeg -y -i "{instrumental}" -i "{vocals}" '
        f'-filter_complex "[0:a]volume=0.8[a0];[1:a]volume=1.2[a1];[a0][a1]amix=inputs=2:duration=longest, loudnorm" '
        f'"{output}"'
    )

    return output