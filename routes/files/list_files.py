from flask import request
from utils.files import get_server_files
from utils.server_methods import send_response
from utils.database import Database

def route(): 
    server_id = request.args.get("id")
        
    return send_response(content=get_server_files(server_id))