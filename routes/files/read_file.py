import os

from flask import request
from utils.files import read_file_content
from utils.server_methods import send_response
from utils.database import Database

def route():
    server_id = request.args.get("id")
    path = request.args.get("path")
    file_name = request.args.get("name")
    
    content = read_file_content(path=os.path.join(path, file_name), server_id=server_id)
    
    return send_response(content=content) if content != None else send_response(success=False, code=500)