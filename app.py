from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from configs import settings


app: FastAPI = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
)
app.mount("/static", StaticFiles(directory="static"), name="static")
