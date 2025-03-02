from flask import request
from utils.server_methods import communicate_command, remove_process, server_exists
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get(key="id")
    
    exists = server_exists(server_id, db.get_server(server_id))
    
    if exists != None:
        return exists
    
    response = communicate_command("stop", server_id)
        
    remove_process(server_id)
        
    return response