import os

from flask import request

from utils.server_methods import send_response, check_mods
from utils.config import SERVERS

def get_server_mods(server_id: str):
    data = []
    
    path = os.path.join(SERVERS, server_id, "mods")
        
    for _, _, filesnames in os.walk(path):
        data.extend(filesnames)
        
    mods_checked = check_mods(path)
        
    return send_response(content=data) if mods_checked == None else mods_checked

def route(): 
    server_id = request.args.get("id")
        
    return get_server_mods(server_id)