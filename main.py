from server import Server
from utils.database import Database
from utils.config import server_exists
from flask import Flask, Response, request

class API:
    def __init__(self):
        self.app = Flask(import_name=__name__)
        self.db = Database()
        self.all_process = {}
        
        self.app.add_url_rule("/start", "start", self.start_server) # Takes server_id: str
        self.app.add_url_rule("/stop", "stop", self.stop_server) # Takes server_id: str
        self.app.add_url_rule("/create", "create", self.create_server) # Takes game_version: str
        self.app.add_url_rule("/get_all_servers", "get_all_servers", self.get_all_servers)
        self.app.add_url_rule("/get_server", "get_server", self.get_server)
        self.app.add_url_rule("/send_command", "send_command", self.send_command)
        self.app.add_url_rule("/is_server_started", "is_server_started", self.is_server_started)

    def send_response(self, content):
        response = Response(content)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    def get_all_servers(self):
        servers = self.db.get_all_server()
        return self.send_response(content=servers)

    def get_server(self):
        server_id = request.args.get("id")
        server = self.db.get_server(server_id=server_id)
        return self.send_response(content=server)

    def is_server_started(self):
        server_id = request.args.get("id")

        if server_id in self.all_process:
            return self.send_response("true")
        else:
            return self.send_response("false")
        
    def create_server(self):
        game_version = request.args.get("game_version")
        server_id = self.db.insert_server(game_version=game_version)
        Server(server_db=self.db.get_server(server_id=server_id), server_id=server_id)
        
        return self.send_response(content="success")
         
    def start_server(self):
        server_id = request.args.get(key="id")
        db_server = self.db.get_server(server_id=server_id)
        
        if db_server == None:
            return self.send_response(content="Server does not exist.")
        
        server = Server(server_db=db_server, server_id=server_id)
        process = server.start()
            
        self.all_process[server_id] = process
            
        return self.send_response(content="success")
        
    def stop_server(self):
        server_id = request.args.get(key="id")
        response = self.communicate_command("stop", server_id)
        
        return response
        
    def send_command(self):
        server_id = request.args.get(key="id")
        command = request.args.get(key="command")
    
        response = self.communicate_command(command, server_id)
        
        return response
        
    def communicate_command(self, query: str, server_id: str):
        db_server = self.db.get_server(server_id=server_id)
        
        if db_server == None:
            return self.send_response(content="Server does not exist.")
        if server_id not in self.all_process:
            return self.send_response(content="Server is not started.")
        
        process = self.all_process[server_id]
        process.communicate(query)
        
        return self.send_response(content="success")
        
    def run(self):
        self.app.run(host="0.0.0.0")

if __name__ == "__main__":
    api = API()
    api.run()