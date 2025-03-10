from flask import request
from utils.server_methods import communicate_command, remove_process
from utils.database import Database

def route():
    db = Database()
    
    server_id = request.args.get(key="id")
    
    remove_process(server_id)
    
    response = communicate_command("stop", server_id)
                
    return response