from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
from app.schemas import ProcessRequest
from app.pipeline_runner import run_pipeline_async, get_status

router = APIRouter()

@router.post("/process")
def process(req: ProcessRequest):
    job_id = run_pipeline_async(url=req.youtube_url)
    return {"job_id": job_id, "status": "processing"}

@router.post("/upload-process")
async def upload_and_process(file: UploadFile = File(...)):
    os.makedirs("data/input", exist_ok=True)
    upload_path = f"data/input/{file.filename}"

    # Save uploaded file
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run the same background pipeline but bypassing YouTube
    job_id = run_pipeline_async(url=None, input_path=upload_path)
    return {"job_id": job_id, "status": "processing"}

@router.get("/status/{job_id}")
def status(job_id: str):
    return get_status(job_id)

@router.get("/download/{job_id}")
def download(job_id: str):
    job = get_status(job_id)
    if "outputs" not in job:
        return {"error": "Not ready"}

    return FileResponse(job["outputs"]["zip"], filename="result.zip")