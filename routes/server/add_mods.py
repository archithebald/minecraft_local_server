from flask import request
from server import Server

from utils.database import Database
from utils.server_methods import send_response

def route():
    db = Database()
    
    server_id = request.args.get("id")
    mods_ids = request.args.get("mods_ids")
    
    server = Server(server_db=db.get_server(server_id), server_id=server_id)
    server.forge_app.download_mods(ids=list(mods_ids))
    
    return send_response(params={"server_id": server_id, "mods_ids": mods_ids})