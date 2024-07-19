from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

import toml
from pathlib import Path

class Config:
    def __init__(self):
        self.file_path = Path("./config/config.toml")
    
    def get_config(self):
        return toml.loads(self.file_path.read_text())
    
    @property
    def redirects(self) -> dict:
        data = self.get_config()
        return data.get("redirects", {})
    
    @property
    def files(self) -> dict:
        data = self.get_config()
        return data.get("files", {})

    @property
    def projects(self) -> dict:
        data = self.get_config()
        return data.get("projects", {})