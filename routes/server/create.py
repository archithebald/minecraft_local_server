from utils.config import send_response
from flask import request
from server import Server
from utils.database import Database

def route():
    db = Database()

    game_version = request.args.get("game_version")
    description = request.args.get("description")
    server_version = request.args.get("server_version")
    ram_max = request.args.get("ram_max")
    ram_min = request.args.get("ram_min")

    server_id = db.insert_server(game_version=game_version, description=description, ram_max=ram_max, ram_min=ram_min, server_version=server_version)
    Server(server_db=db.get_server(server_id=server_id), server_id=server_id)
        
    return send_response(content="success")