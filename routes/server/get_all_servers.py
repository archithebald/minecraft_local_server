from utils.server_methods import send_response
from utils.database import Database

def route():
    db = Database()
    
    servers = db.get_all_server()
    return send_response(content=servers)