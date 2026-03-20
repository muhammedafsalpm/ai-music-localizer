# Music Localization API

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## Workflow
1. POST /process with YouTube URL
2. GET /status/{job_id}
3. Edit lyrics DOCX manually
4. Complete voice + mixing
5. Download results

## Notes
- Voice conversion uses RVC (manual step)
- Mixing done externally (DAW recommended)
- Designed for local, open-source pipeline