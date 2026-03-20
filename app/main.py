from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Music Localization API")

app.include_router(router)