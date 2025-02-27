from utils.config import send_response
from flask import request
from server import Server
from utils.database import Database
from utils.server_methods import communicate_command

def route():
    server_id = request.args.get(key="id")
    command = request.args.get(key="command")
    
    response = communicate_command(command, server_id)
        
    return response