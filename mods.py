import requests

class Modpack:
    def __init__(self, forge_link: str = None, modpack = None):
        self.name = ""
        self.summary = ""
        self.author = ""
        self.avatarUrl = ""
        self.categories = {}
        self.forge_class = {}
        self.creationDate = ""
        self.downloads = 0
        self.fileSize = 0
        self.gameVersion = ""
        self.id = ""
        self.isAvailableForDownload = None
        self.latestFileDetails = {}
        self.slug = ""
        self.thumbnails = {}
        self.updateDate = None
        self.websiteRecentFiles = {}
        self.download_link = ""

        if forge_link:
            pass
        
        if modpack:
            for attr in dir(self):
                if attr in modpack:
                    setattr(self, attr, modpack[attr])

            self.download_link = f"https://www.curseforge.com/minecraft/modpacks/{self.slug}/download/{self.latestFileDetails["gameVersionTypeIds"][0]}"
            
    def download(self):
        pass        
    
class Mod:
    def __init__(self, id: int, game_version: str):
        self.id = id
        self.game_version = game_version
        
        self.get_mod()
        
        self.versions = self.mod["versions"]
        self.slug = self.mod["links"][0]["link"].split("/")[-1]
        
        self.compatible_files = []
        
        self.get_file_link()
    
    def get_mod(self):
        URL = f"https://api.modpacks.ch/public/mod/{str(self.id)}"
        
        try:
            self.mod = requests.get(URL).json()
        except Exception as e:
            print(e)
            
    def get_file_link(self):
        for version in self.versions:
            self.compatible_files.extend([version for target in version["targets"] if target["version"] == self.game_version])

print(Mod(id=238222, game_version="1.12.2").mod_link)