from flask import request
from utils.server_methods import communicate_command, remove_process

def route():
    server_id = request.args.get(key="id")
    response = communicate_command("stop", server_id)
        
    remove_process(server_id)
        
    return response