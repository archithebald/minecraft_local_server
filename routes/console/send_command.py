from utils.config import send_response
from flask import request
from server import Server
from utils.database import Database
from utils.server_methods import communicate_command, server_exists

def route():
    server_id = request.args.get(key="id")
    command = request.args.get(key="command")
    
    exists = server_exists(server_id, Database().get_server(server_id))
    
    if exists != None:
        return exists
    
    response = communicate_command(command, server_id)
        
    return response