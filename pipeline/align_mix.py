import os

def align_and_mix(vocals, instrumental):
    output = "data/output/final.wav"

    os.system(
        f'ffmpeg -y -i "{instrumental}" -i "{vocals}" '
        f'-filter_complex amix=inputs=2:duration=longest "{output}"'
    )

    return output