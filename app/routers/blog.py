from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException

from markdown import Markdown

from ..blog import Blog
from ..ctx import ContextBuild

router = APIRouter(prefix = "/blog")

markdown = Markdown(extensions = ["fenced_code", "sane_lists"])
templates = Jinja2Templates(directory = "templates")

blog = Blog()

@router.get("")
@router.get("/")
async def blog_page(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas • Blog",
        description = "My blog :3",
        image_url = "https://ananas.moe/me.webp"
    )

    return templates.TemplateResponse(
        "blogs.html", {
            **context.data,
            "blogs": blog.blogs 
        }
    )

@router.get("/{slug}")
async def blog_id(request: Request, slug: str):
    for post in blog.blogs:
        if post["slug"] == slug:
            context = ContextBuild(
                request = request,
                title = "Ananas • Blog",
                description = post.get("title"),
                image_url = post.get("thumbnail", "https://ananas.moe/me.webp")
            )

            post["content"] = markdown.convert(
                blog.content(
                    post.get("file")
                )
            ).replace("./", f"./{post['slug']}/")

            return templates.TemplateResponse(
                "blog.html", {
                    **context.data,
                    "post": post
                }
            )
    
    raise HTTPException(404, "Post not Found")

@router.get("/{slug}/{file}")
async def cdn_redirect(request: Request, slug: str, file: str):
    return RedirectResponse(f"https://cdn.ananas.moe/blog/{slug}/{file}")