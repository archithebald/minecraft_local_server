from flask import request
from server import Server
from utils.database import Database
from utils.server_methods import communicate_command, send_response

def route():
    server_id = request.args.get(key="id")
    command = request.args.get(key="command")

    
    response = communicate_command(command, server_id)
        
    return response