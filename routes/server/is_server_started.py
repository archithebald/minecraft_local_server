from utils.config import send_response
from utils.server_methods import get_processes, server_exists
from flask import request
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get("id")
    
    exists = server_exists(server_id=server_id, server_db=db.get_server(server_id=server_id))
    
    if exists != None:
        return exists

    if server_id in get_processes():
        return send_response("true")
    else:
        return send_response("false")