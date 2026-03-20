import uuid

jobs = {}

def create_job():
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "created"}
    return job_id

def update_status(job_id, status, outputs=None):
    jobs[job_id]["status"] = status
    if outputs:
        jobs[job_id]["outputs"] = outputs

def get_job(job_id):
    return jobs.get(job_id, {"error": "not found"})