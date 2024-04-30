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
    
    async def __read_lang(self, lang):
        file = str(self.lang_path.joinpath(lang))

        async with aiofiles.open(file, "r") as f:
            file = await f.read()
            await f.close()
            
            file = json.loads(file)

        return file
    
    async def get_lang(self, lang: str):
        config = await self.get_config()

        for config_language in config["languages"]:
            
            if config_language["language"] == lang:
                
                json_file = f"{lang}.json"

                does_exist = self.lang_path.joinpath(json_file)

                if does_exist.exists():
                    language = await self.__read_lang(json_file)

                    return language

        return None