import pymongo, json
from bson import ObjectId

class Singleton:
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(Singleton):
    def __init__(self):
        super().__init__()
        
        try:
            self.CLIENT_CONN = pymongo.MongoClient("mongodb://localhost:27017/")
            self.DATABASE_NAME = "minecraft_servers"    
            self.SERVERS_COL_NAME = "servers"
            
            if self.DATABASE_NAME not in self.CLIENT_CONN.list_database_names():
                return FileNotFoundError("Database not found.")
            else:
                print(">>> Servers database exists. ✅")
                self.DATABASE = self.CLIENT_CONN["minecraft_servers"]
                
            if self.SERVERS_COL_NAME not in self.DATABASE.list_collection_names():
                return FileNotFoundError("Servers collection not found.")
            else:
                self.SERVERS = self.DATABASE[self.SERVERS_COL_NAME]
        except Exception as e:
            print(">>> {}".format(e))
            
    def get_server(self, server_id: str):
        try:
            server = self.SERVERS.find_one(filter={"_id": ObjectId(server_id)})
            return json.dumps({**server, "_id": str(server["_id"])})
        except Exception as e:
            print(">>> {}".format(e))
            
    def insert_server(self, game_version: str, description: str = "A minecraft server.", ram_min: int = 1024, ram_max: int = 2048, server_version: str = "Vanilla"):
        try:
            document = {
                "description": description,
                "game_version": game_version,
                "ram_min": ram_min,
                "server_version": server_version,
                "ram_max": ram_max
            }
            inserted = self.SERVERS.insert_one(document=document)
            return inserted.inserted_id
        except Exception as e:
            print(">>> {}".format(e))
            
    def get_all_server(self):
        return json.dumps(
            [{**server, "_id": str(server["_id"])} for server in self.SERVERS.find()]
        )