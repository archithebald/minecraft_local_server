import pymongo, json, os
from bson import ObjectId
from pymongo.errors import PyMongoError

from utils.files import delete_folder
from utils.config import SERVERS, send_response

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
            
    def server_exists(self, server_id: str):
        if server_id == None:
            return send_response(content="Missing id parameter", success=False, code=400)
        
        server_db = self.SERVERS.get_server(server_id)
        
        if server_db == None:
            return send_response(content="Server doesn't exist", success=False, code=404)
        
        return None
            
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
        
    def safe_delete_server(self, server_id):
        with self.CLIENT_CONN.start_session() as session:
            try:
                with session.start_transaction():
                    result = self.SERVERS.delete_one({"_id": server_id}, session=session)
                    
                    if result.deleted_count == 0:
                        return send_response(content="Server not found in the database.", success=False, code=404)
                    
                    folder_path = os.path.join(SERVERS, server_id)
                    folder_status = delete_folder(path=folder_path)
                    
                    if not folder_status:
                        session.abort_transaction()
                        return send_response(content="Couldn't delete server files.", success=False, code=500, error="Folder deletion failed")
                    
                    return send_response()
            except PyMongoError as e:
                session.end_session()
                return send_response(content="Database error occurred.", success=False, code=500, error=str(e))
            except Exception as e:
                return send_response(content="An error occurred.", success=False, code=500, error=str(e))