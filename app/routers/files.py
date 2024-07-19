from __future__ import annotations

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates

from ..config import Config
from pathlib import Path

__all__ = ("file", )

templates = Jinja2Templates(directory = "./temp")

config = Config()
files = APIRouter()

@files.get("/file/{file_id}")
async def file(request: Request, file_id: str):
    for file in config.files:
        if file.get("id") == file_id:
            file_path = file.get("file")

            uploads = Path("./config", "files", file_path)

            return FileResponse(uploads, filename=file_path)

    raise HTTPException(404)