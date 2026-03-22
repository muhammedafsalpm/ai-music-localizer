import os
import zipfile

def export_outputs(final_path, stems):
    mp3_path = final_path.replace(".wav", ".mp3")

    os.system(f'ffmpeg -y -i "{final_path}" "{mp3_path}"')

    return {
        "wav": final_path,
        "mp3": mp3_path,
        "vocals": stems["vocals"],
        "instrumental": stems["instrumental"]
    }


def create_zip(files):
    zip_path = "data/output/result.zip"
    with zipfile.ZipFile(zip_path, 'w') as z:
        for k, f in files.items():
            if os.path.exists(f):
                z.write(f)
    return zip_path