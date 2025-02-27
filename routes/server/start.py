import threading

from utils.config import send_response
from utils.database import Database
from utils.server_methods import add_process

from flask import request
from server import Server

def read_server_cli(self, process):
    try:
        for line in iter(process.stdout.readline, ""):
            print(line.strip())
    except Exception as e:
        print(e)
            
def route():
    db = Database()

    server_id = request.args.get(key="id")
    db_server = db.get_server(server_id=server_id)
        
    if db_server == None:
        return send_response(content="Server does not exist.")
        
    server = Server(server_db=db_server, server_id=server_id)
    process = server.start()
    
    add_process()
    #all_process[server_id] = process
            
    thread = threading.Thread(target=read_server_cli, args=(process,))
    thread.start()
            
    return send_response(content="success")