from utils.server_methods import send_response
from utils.server_methods import get_processes
from flask import request
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get("id")

    if server_id in get_processes():
        return send_response("true")
    else:
        return send_response("false")