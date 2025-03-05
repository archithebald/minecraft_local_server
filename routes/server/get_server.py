from flask import request
from utils.server_methods import send_response
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get("id")
    server_db = db.get_server(server_id)
        
    if server_db is not None:
        return send_response(content=server_db)
    else:
        return send_response(content="Server doesn't exist", success=False, code=404, error="Not found")
    
    