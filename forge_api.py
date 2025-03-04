import requests

from mods import Modpack, Mod

class Forge:
    def __init__(self):
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
            
    def download_mods(ids: list, mods_path: str):
        mods = []
        
        for id in ids:
            mods.append(Mod(id=id))