from flask import request
from utils.config import send_response
from utils.database import Database
from utils.server_methods import server_exists

def route():
    db = Database()
    
    server_id = request.args.get("id")
    server_db = db.get_server(server_id)
    
    exists = server_exists(server_id, server_db)
    
    if exists != None:
        return exists
    
    return send_response(content=server_db)