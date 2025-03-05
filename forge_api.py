import requests, os

from mods import Modpack, Mod
from utils.server_methods import send_response

class Forge:
    def __init__(self, server_path: str, game_version: str):
        self.mods_path = os.path.join(server_path, "mods")
        self.game_version = game_version
        
        self.BASE_URL = "https://www.curseforge.com/api/v1"
            
    def search_mods(self, index: int, **kwargs):
        URL = self.BASE_URL + f"/mods/search?gameId=432&index={index}"
        
        for k, v in kwargs.items():
            URL += f"&{k}={v}"
        
        try:
            response = requests.get(url=URL).json()
            
            results = []
            
            for modpack in response["data"]:
                results.append(Modpack(modpack=modpack))
            
            return results
        except Exception as e:
            print(f"Error while fetching modpacks: {e}")
            
    def download_mods(self, ids: list):
        mods = [Mod(mod_id, self.game_version) for mod_id in ids]
        
        for mod in mods:
            try:
                mod.download_mod(path_to_download=self.mods_path, file=mod.compatible_files[0])
            except ValueError as e:
                return send_response(content=f"{mod.slug} has no compatible versions.", success=False, code=404, error=str(e))