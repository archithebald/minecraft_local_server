import os, shutil

from flask import request

from utils.database import Database
from utils.server_methods import send_response
from utils.config import SERVERS

def delete_server(server_id: str):
    path = os.path.join(SERVERS, server_id)
    
    for root, _, files_names in os.walk(path):
        for file in files_names:
            os.remove(os.path.join(root, file))
                
    shutil.rmtree(path)

def route():
    db = Database()
    
    server_id = request.args.get("id")
    
    db.delete_server(server_id)
    delete_server(server_id)
    
    return send_response()