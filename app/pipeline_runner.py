import threading
import os
import subprocess
import traceback
import os
import subprocess
from jobs.job_store import create_job, update_status, get_job

from pipeline.download import download_audio
from pipeline.separation import separate_audio
from pipeline.lyrics import extract_lyrics, create_docx
from pipeline.preprocess import preprocess_vocals
from pipeline.voice import run_voice_conversion
from pipeline.align_mix import align_and_mix
from pipeline.export import export_outputs, create_zip
from pipeline.singing import generate_singing


def run_pipeline_async(url=None, input_path=None):
    job_id = create_job()
    thread = threading.Thread(target=run_pipeline, args=(job_id, url, input_path))
    thread.start()
    return job_id


def run_pipeline(job_id, url, input_path):
    try:
        if input_path:
            update_status(job_id, "processing_upload")
            audio = "data/input/song.wav"
            if os.path.exists(audio) and audio != input_path:
                os.remove(audio)
            
            # Convert uploaded file (like mp3) to wav gracefully
            subprocess.run(
                ["ffmpeg", "-y", "-i", input_path, audio],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        else:
            update_status(job_id, "downloading")
            audio = download_audio(url)

        update_status(job_id, "separating")
        stems = separate_audio(audio)

        update_status(job_id, "extracting_lyrics")
        lyrics_txt = extract_lyrics(stems["vocals"])

        update_status(job_id, "creating_docx")
        docx_path = create_docx(lyrics_txt)

        update_status(job_id, "waiting_for_lyrics_edit", {
            "docx": docx_path,
            "stems": stems,
            "stage": "waiting"
        })

        return  # HARD STOP (MANDATORY)

    except Exception as e:
        update_status(job_id, f"failed: {str(e)}\n{traceback.format_exc()}")


def resume_pipeline(job_id):
    job = get_job(job_id)
    data = job.get("outputs", {})

    stems = data.get("stems")

    if not stems:
        raise Exception("Missing stems in job state")

    update_status(job_id, "singing_generation")

    # STEP: user must provide singing
    synth = generate_singing()

    if not os.path.exists(synth):
        raise Exception("Synth file missing")

    update_status(job_id, "preprocessing")
    clean = preprocess_vocals(synth)

    update_status(job_id, "voice_conversion")
    generated = run_voice_conversion(clean)

    if not os.path.exists("data/processed/generated_vocals.wav"):
        raise Exception("RVC output missing")

    update_status(job_id, "mixing")
    final = align_and_mix(generated, stems["instrumental"])

    update_status(job_id, "exporting")
    outputs = export_outputs(final, stems)

    zip_path = create_zip(outputs)

    update_status(job_id, "completed", {"zip": zip_path})


def get_status(job_id):
    return get_job(job_id)