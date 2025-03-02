from utils.config import send_response
from flask import request
from server import Server
from utils.database import Database

all_process = {}

db = Database()



def add_process(server_id: str, process):
    all_process[server_id] = process
    
def remove_process(server_id: str):
    all_process.pop(server_id)
    
def get_processes():
    return all_process

def server_exists(server_id: str, server_db):
    if server_id == None:
        return send_response(content="Missing id parameter", success=False, code=400)
    
    if server_db == None:
        return send_response(content="Server doesn't exist", success=False, code=404)
    
    return None

def communicate_command(query: str, server_id: str):
    db_server = db.get_server(server_id=server_id)
    
    exists = server_exists(server_id, db_server)
    
    if exists != None:
        return exists
    
    if server_id not in all_process:
        return send_response(content="Server is not started.")
        
    process = all_process[server_id]
    process.communicate(query)
        
    return send_response(content="success")