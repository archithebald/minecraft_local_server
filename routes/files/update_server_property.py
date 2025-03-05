from flask import request
from server import Server
from utils.database import Database
from utils.server_methods import send_response

def route():
    db = Database()
    
    server_id = request.args.get(key="id")
    db_server = db.get_server(server_id=server_id)
        
    updated_name = request.args.get(key="updated_name")
    updated_value = request.args.get(key="updated_value")
        
    server = Server(server_db=db_server, server_id=server_id, init=False)
        
    return send_response(content=server.update_property(updated_name, updated_value))