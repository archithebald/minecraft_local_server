import requests, os

from mods import Modpack, Mod

from utils.config import send_response
from utils.files import delete_file

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
           
    def get_mods(self, ids: list):
        return [Mod(mod_id, self.game_version) for mod_id in ids]
            
    def download_mods(self, ids: list):
        wrong_ids = []
        
        for mod in self.get_mods(ids):
            try:
                mod.download_mod(path_to_download=self.mods_path, file=mod.compatible_files[0])
            except IndexError:
                wrong_ids.append(mod.id)
        
        if wrong_ids:
            return send_response(content=str(wrong_ids), success=False, code=200, error="Some mods ids are wrong")
        else:
            return send_response()
        
    def remove_mods(self, slugs: list):
        wrong_slugs = []
        
        for slug in slugs:
            try:
                root, dirnames, filenames = next(os.walk(self.mods_path))
                if slug in filenames:
                    delete_file(os.path.join(self.mods_path, slug+".jar"))
            except FileNotFoundError or Exception:
                wrong_slugs.append(slug)
        
        if wrong_slugs:
            return send_response(content=str(wrong_slugs), success=False, code=200, error="Some mods slugs are wrong")
        else:
            return send_response()