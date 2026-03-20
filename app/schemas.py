from pydantic import BaseModel

class ProcessRequest(BaseModel):
    youtube_url: str