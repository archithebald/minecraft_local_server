import threading

from utils.database import Database
from utils.server_methods import add_process, send_response, is_a_process

from flask import request
from server import Server

def read_server_cli(process):
    try:
        for line in iter(process.stdout.readline, ""):
            print(line.strip())
    except Exception as e:
        print(e)
            
def route():
    db = Database()
    
    server_id = request.args.get(key="id")
    db_server = db.get_server(server_id=server_id)
        
    if is_a_process(server_id=server_id):
        return send_response(content="Server already started", code=409, success=False, error="Conflict")
        
    server = Server(server_db=db_server, server_id=server_id)
    process = server.start()
    
    add_process(server_id, process)
            
    thread = threading.Thread(target=read_server_cli, args=(process,))
    thread.start()
            
    return send_response(content="success")