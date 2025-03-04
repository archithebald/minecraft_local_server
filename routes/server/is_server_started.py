from utils.server_methods import send_response
from utils.server_methods import get_processes, server_exists
from flask import request
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get("id")

    if server_id in get_processes():
        return send_response("true", params={"server_id": server_id})
    else:
        return send_response("false")