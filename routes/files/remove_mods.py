import os

from flask import request
from server import Server

from utils.database import Database
from utils.server_methods import check_mods

def route():
    db = Database()
    
    server_id = request.args.get("id")
    slugs = request.args.get("slugs").split(",")
    
    server = Server(server_db=db.get_server(server_id), server_id=server_id)
    
    checked = check_mods(server.mods_path)
    
    return server.forge_app.remove_mods(slugs=slugs) if checked == None else checked