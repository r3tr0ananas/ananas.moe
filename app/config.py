from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

import json
import aiofiles
from pathlib import Path

class Config:
    def __init__(self):
        self.config_path = Path("./config/config.json")
        self.lang_path = Path("./config/lang/")
    
    async def get_config(self):
        async with aiofiles.open(str(self.config_path), "r") as f:
            file = await f.read()
            await f.close()
            
            file = json.loads(file)

        return file