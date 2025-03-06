from flask import request
from server import Server

from utils.server_methods import check_mods

def route():
    server_id = request.args.get("id")
    mods_ids = request.args.get("mods_ids").split(",")
    
    server = Server(server_id=server_id)
    
    checked = check_mods(server.mods_path)
    
    return server.forge_app.download_mods(ids=mods_ids) if checked == None else checked