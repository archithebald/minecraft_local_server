import os

from flask import request
from utils.files import get_server_file_path
from utils.server_methods import send_response
from utils.database import Database

def route():
    server_id = request.args.get("id")
    path = request.args.get("path")
    file_name = request.args.get("name")
    updated_text = request.args.get("updated")
    
    path = get_server_file_path(server_id, path, file_name)
    
    try:
        f = open(path, "w", encoding="utf-8")
        f.write(updated_text)
        
        return send_response()
    except FileNotFoundError:
        return send_response(content="File not found", success=False, code=404)
    except Exception:
        return send_response(success=False, code=500)