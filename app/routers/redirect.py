"""
Code from [devgoldy.xyz](https://github.com/THEGOLDENPRO/devgoldy.xyz/)
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException

from ..config import Config

__all__ = ("router", )

config = Config()
router = APIRouter()

templates = Jinja2Templates(directory = "./templates")

@router.get("/github")
async def github(request: Request):
    return templates.TemplateResponse(
        "redirect.html", {
            "request": request,
            "title": "My GitHub",
            "description": "Check out my GitHub",
            "image_url": "https://avatars.githubusercontent.com/u/132799819",
            "url": "https://github.com/R3tr0Ananas"
        }
    )

@router.get("/codeberg")
async def codeberg(request: Request):
    return templates.TemplateResponse(
        "redirect.html", {
            "request": request,
            "title": "My Codeberg",
            "description": "Check out my Codeberg",
            "image_url": "https://ananas.moe/me.webp",
            "url": "https://codeberg.org/bananas"
        }
    )

@router.get("/r/{redirect_id}")
async def custom(request: Request, redirect_id: str):
    for redirect in config.redirects:
        if redirect.get("id") == redirect_id:

            return templates.TemplateResponse(
                "redirect.html", {
                    "request": request,
                    "title": redirect.get("title"),
                    "description": redirect.get("description"),
                    "image_url": redirect.get("image_url"),
                    "url": redirect.get("url")
                }
            )

    raise HTTPException(404)