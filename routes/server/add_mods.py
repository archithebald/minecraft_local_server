import os

from flask import request
from server import Server

from utils.database import Database
from utils.server_methods import send_response

def route():
    db = Database()
    
    server_id = request.args.get("id")
    mods_ids = request.args.get("mods_ids").split(",")
    
    server = Server(server_db=db.get_server(server_id), server_id=server_id)
    
    if not os.path.exists(server.mods_path):
        return send_response(content="Mods path doesn't exist, please start server first.", error="File Error", success=False, code=404)
    
    return server.forge_app.download_mods(ids=list(mods_ids))