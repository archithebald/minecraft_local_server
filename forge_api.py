import requests

from mods import Modpack

class Forge:
    def __init__(self):
        self.BASE_URL = "https://www.curseforge.com/api/v1"
    
    def search_modpacks(self, query: str = "", gameId: str = "432", index: int = 0, classId: str = "4471", pageSize: str = "20", sortField: str = "1") -> list:
        URL = self.BASE_URL + f"/mods/search?gameId={gameId}&index={index}&classId={classId}&filterText={query}&pageSize={pageSize}&sortField={sortField}"
        
        try:
            response = requests.get(url=URL).json()
            
            results = []
            
            for modpack in response["data"]:
                results.append(Modpack(modpack=modpack))
            
            return results
        except Exception as e:
            print(f"Error while fetching modpacks: {e}")