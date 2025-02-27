import json

from utils.config import send_response
from flask import request
from server import Server
from utils.database import Database

def route():
    db = Database()

    server_id = request.args.get(key="id")
    db_server = db.get_server(server_id=server_id)
        
    updated_properties = json.loads(request.args.get("updated_properties"))
        
    if db_server == None:
        return send_response(content="Server does not exist.")
        
    server = Server(server_db=db_server, server_id=server_id, init=False)

    for key, value in updated_properties.items():
        server.update_property(key, value)
            
    return send_response()