from __future__ import annotations

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates

from ..config import Config
from pathlib import Path

__all__ = ("r_files", )

templates = Jinja2Templates(directory = "./temp")
config = Config()
r_files = APIRouter()

@r_files.get("/file/{file_id}")
async def file(request: Request, file_id: str):
    js = await config.get_files()

    if file_id in js:
        file_to_send = js[file_id]

        uploads = await Path("./config", "files", file_to_send)

        return FileResponse(uploads, filename=file_to_send)

    raise HTTPException(404)