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
    def __init__(self, forge_link: str):
        pass