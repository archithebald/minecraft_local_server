import requests, os, subprocess, json, signal, psutil

from time import sleep
from utils.config import START_SCRIPT, SERVERS
from forge_api import Forge, Modpack

class Server:
    def __init__(self, server_db, server_id: str = None):
        if type(server_db) == str:
            server_db = json.loads(server_db)
         
        self.game_version = server_db["game_version"]
        self.jar_name = "server.jar"
        self.id = server_id
        self.path = os.path.join(SERVERS, str(self.id))
        self.jar_path = os.path.join(self.path, self.jar_name)
        self.eula_path = os.path.join(self.path, "eula.txt")
        self.ram_min = server_db["ram_min"]
        self.ram_max = server_db["ram_max"]

        if not os.path.exists(self.path):
            print(">>> Server instance not found. ❓")
            print(f">>> Creating a server instance. 🔧 Version: {self.game_version}")
            os.mkdir(path=self.path)
            self.create_instance()
        else:
            print(">>> Server instance found. ✅")
            
        self.forge_app = Forge()
            
        self.update_properties()        
        self.init_server()
    
    def update_properties(self):
        pass
    
    def create_instance(self):
        self.version = self.get_version()
        self.jar_url = self.get_jar_url()
        self.download_jar()

    def get_version(self):
        link = "https://piston-meta.mojang.com/mc/game/version_manifest.json"
        
        response = requests.get(link).json()
        
        return next((version for version in response["versions"] if version["id"] == self.game_version), None)

    def get_jar_url(self):
        version_link = self.version["url"]
        
        self.version_metadata = requests.get(version_link).json()
        
        return self.version_metadata["downloads"]["server"]["url"]

    def download_jar(self):
        response = requests.get(self.jar_url, stream=True)
        
        if response.status_code == 200:
            with open(self.jar_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f">>> Server instance downloaded at: {self.jar_path} ✅")
        else:
            print(f">>> Failed to download server instance. Status code: {response.status_code} ❌")
            
    def get_pid(self):
        jar_name = self.jar_path.split("\\")[-1]
        cmd = f'wmic process where "name=\'java.exe\'" get ProcessId'

        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        real_pid = [int(pid) for pid in result.stdout.split() if pid.isdigit()]

        if real_pid:
            return real_pid[0]
        else:
            return None
            
    def start(self):
        try:
            #command = ["start", START_SCRIPT, str(self.ram_max), str(self.ram_min), self.jar_path]
            command = ["java", f"-Xmx{str(self.ram_max)}M", f"-Xms{str(self.ram_min)}M", "-jar", self.jar_path, "nogui"]
            self.process = subprocess.Popen(
                command,
                cwd=self.path,
                text=True,
                stdin=subprocess.PIPE, 
                universal_newlines=True
            )
            print(">>> Server started. ✅")
            
            self.accept_eula()
            
            return self.process
        except Exception as e:
            print(">>> Error while starting server. ❌")
            print(f">>> Error : {e}")
            return False

    def stop(self):
        try:
            print(">>> Stopping server")
            self.process.communicate("stop")
        except Exception as e:
            print(e)
            return False
    
    def send_command(self, query):
        try:
            print(">>> Sending command")
            self.process.communicate(query)
        except Exception as e:
            print(e)
    
    def check_eula(self):
        eula_file = open(self.eula_path, "r").read()
        lines = eula_file.splitlines()
        accepted = bool(next(line.split("=")[1] for line in lines if "eula" in line))
        return accepted
        
    def accept_eula(self):
        try:
            eula_file = open(self.eula_path, "w")
            eula_file.write("eula=true")
            print("Eula accepted. ✅")
        except Exception as e:
            print("Failed while accepting eula. ❌")
            print(f"Error: {e}")
        
    def init_server(self):
        sleep(2)
        if os.path.exists(self.eula_path):
            self.accept_eula()