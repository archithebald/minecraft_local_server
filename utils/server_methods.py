from flask import make_response
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

def server_exists(server_id: str):
    if server_id == None:
        return send_response(content="Missing id parameter", success=False, code=400)
    
    server_db = db.get_server(server_id)
    
    if server_db == None:
        return send_response(content="Server doesn't exist", success=False, code=404)
    
    return None

def communicate_command(query: str, server_id: str):    
    exists = server_exists(server_id)
    
    if exists != None:
        return exists
    
    if server_id not in all_process:
        return send_response(content="Server is not started.")
        
    process = all_process[server_id]
    process.communicate(query)
        
    return send_response(content="success")

def send_response(content: str = "", headers: dict = {}, success: bool = True, code: int = None, error: str = ""):    
    message = "success" if success else "error"
    
    if code == None:
        code = 200 if success else 400
        
    if message == "error":
        response = make_response({"message": message, "data": content, "error": error})   
    else:
        response = make_response({"message": message, "data": content})    
 
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.status_code = code
    
    for header in headers.items():
        response.headers[header]
    
    return response