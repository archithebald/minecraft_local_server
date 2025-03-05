from utils.config import send_response

all_process = {}

def add_process(server_id: str, process):
    all_process[server_id] = process
    
def remove_process(server_id: str):
    if server_id in all_process:
        all_process.pop(server_id)
    
def get_processes():
    return all_process

def is_a_process(server_id: str):
    return True if server_id in get_processes().keys() else False

def communicate_command(query: str, server_id: str):           
    if server_id not in all_process:
        return send_response(content="Server is not started or doesn't exist.", error="Not found", code=404, success=False)
            
    process = all_process[server_id]
    process.communicate(query)
            
    return send_response(content="success")