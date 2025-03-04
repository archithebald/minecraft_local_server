import threading

from utils.database import Database
from utils.server_methods import add_process, send_response

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
        
    exists = server_exists(server_id, db_server)
    
    if exists != None:
        return exists
        
    server = Server(server_db=db_server, server_id=server_id)
    process = server.start()
    
    add_process(server_id, process)
            
    thread = threading.Thread(target=read_server_cli, args=(process,))
    thread.start()
            
    return send_response(content="success")