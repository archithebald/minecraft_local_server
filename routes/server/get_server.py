from flask import request
from utils.server_methods import send_response
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get("id")
    server_db = db.get_server(server_id)
        
    return send_response(content=server_db, params={"server_id": server_id})