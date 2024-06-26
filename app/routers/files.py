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
    live_config = await config.get_config()

    js = live_config.get("files", {})

    if file_id in js:
        file_to_send = js[file_id]

        uploads = Path("./config", "files", file_to_send)

        return FileResponse(uploads, filename=file_to_send)

    raise HTTPException(404)