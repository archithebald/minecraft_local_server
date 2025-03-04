from flask import request
from server import Server
from utils.database import Database
from utils.server_methods import send_response

def route():
    db = Database()

    server_id = request.args.get(key="id")
    db_server = db.get_server(server_id=server_id)
        
    if db_server == None:
        return send_response(content="Server does not exist.")
        
    server = Server(server_db=db_server, server_id=server_id, init=False)
        
    return send_response(content=server.get_properties())