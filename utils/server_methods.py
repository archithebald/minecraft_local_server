from utils.config import send_response
from flask import request
from server import Server
from utils.database import Database

all_process = {}

def communicate_command(query: str, server_id: str):
    db = Database()

    db_server = db.get_server(server_id=server_id)
        
    if db_server == None:
        return send_response(content="Server does not exist.")
    if server_id not in all_process:
        return send_response(content="Server is not started.")
        
    process = all_process[server_id]
    process.communicate(query)
        
    return send_response(content="success")

def add_process(server_id: str, process):
    all_process[server_id] = process
    
def remove_process(server_id: str):
    all_process.pop(server_id)
    
def get_processes():
    return all_process