from flask import request
from utils.files import get_server_files
from utils.server_methods import server_exists
from utils.database import Database
from utils.config import send_response

def route(): 
    server_id = request.args.get("id")
    
    exists = server_exists(server_id, Database().get_server(server_id))
    
    if exists != None:
        return exists
        
    return send_response(content=get_server_files(server_id))