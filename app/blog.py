from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    ...

import toml
from pathlib import Path

BLOG_PATH = Path("./blog")

class Blog:
    def __init__(self):
        self.toml_file = BLOG_PATH.joinpath("blog.toml")

    def read_toml(self) -> dict:
        return toml.loads(self.toml_file.read_text())

    def content(self, file: str) -> str:
        return BLOG_PATH.joinpath("md", file).read_text()

    @property
    def blogs(self) -> list:
        blogs_toml = self.read_toml()
        
        return blogs_toml.get("post", {})