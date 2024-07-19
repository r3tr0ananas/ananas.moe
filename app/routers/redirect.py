"""
Code from [devgoldy.xyz](https://github.com/THEGOLDENPRO/devgoldy.xyz/)
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException

from ..config import Config

__all__ = ("redirect", )

config = Config()
redirect = APIRouter()

templates = Jinja2Templates(directory = "./templates")

@redirect.get("/github")
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

@redirect.get("/codeberg")
async def codeberg(request: Request):
    return templates.TemplateResponse(
        "redirect.html", {
            "request": request,
            "title": "My Codeberg",
            "description": "Check out my Codeberg",
            "image_url": "https://codeberg.org/avatars/dddd4c528a54500a505d54ebeb41f317c779cc064f14c2c87fd28dbc8341a353",
            "url": "https://codeberg.org/bananas"
        }
    )

@redirect.get("/r/{redirect_id}")
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