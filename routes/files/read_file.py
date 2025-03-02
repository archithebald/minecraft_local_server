import os

from flask import request
from utils.files import read_file_content
from utils.server_methods import server_exists
from utils.database import Database
from utils.config import send_response

def route():
    server_id = request.args.get("id")
    path = request.args.get("path")
    file_name = request.args.get("name")
    
    exists = server_exists(server_id, Database().get_server(server_id))
    
    if exists != None:
        return exists
    
    content = read_file_content(path=os.path.join(path, file_name), server_id=server_id)
    
    return send_response(content=content) if content != None else send_response(success=False, code=500)