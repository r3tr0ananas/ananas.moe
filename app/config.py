import json
import aiofiles

class Config:
    def __init__(self):
        self.path = "./config/config.json"
    
    async def __read(self):
        async with aiofiles.open(self.path, "r") as f:
            config_file = await f.read()
            await f.close()
            
            config_file = json.loads(config_file)

        return config_file

    async def get_redirects(self):
        config = await self.__read()

        return config["redirects"]

    async def get_files(self):
        config = await self.__read()

        return config["files"]


