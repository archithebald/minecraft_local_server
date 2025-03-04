import requests

from utils.files import download_file

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

            self.download_link = f"https://www.curseforge.com/minecraft/modpacks/{self.slug}/download/{self.latestFileDetails['gameVersionTypeIds'][0]}"
            
    def download(self):
        pass        
    
class Mod:
    def __init__(self, id: int, game_version: str, mod_loader: str = "forge"):
        self.id = id
        self.game_version = game_version
        self.mod_loader = mod_loader
        
        self.get_mod()
        
        self.versions = self.mod["versions"]
        self.slug = self.mod["links"][0]["link"].split("/")[-1]
        
        self.compatible_files = []
        
        self.set_compatible_versions()
    
    def get_mod(self):
        URL = f"https://api.modpacks.ch/public/mod/{str(self.id)}"
        
        try:
            self.mod = requests.get(URL).json()
        except Exception as e:
            print(e)
            
    def set_compatible_versions(self):
        for version in self.versions:   
            mod_loaders = []   
            game_versions = []  
            
            for target in version["targets"]:
                if target["type"] == "modloader":
                    mod_loaders.append(target["version"])
                else:
                    game_versions.append(target["version"])
                    
            if self.game_version in game_versions and self.mod_loader in mod_loaders:
                self.compatible_files.append(version)
                
    def download_mod(self, path_to_download: str, file):
        download_file(url=file["url"], path_to_download=path_to_download, file_name=self.slug, extension="jar")