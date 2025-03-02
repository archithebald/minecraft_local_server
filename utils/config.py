import os

from flask import make_response

ROOT = os.getcwd()

SERVERS = os.path.join(ROOT, "servers")
ROUTES = os.path.join(ROOT, "routes")

def server_exists(server_id):
    return os.path.exists(os.path.join(SERVERS, server_id))

def send_response(content: str = "", headers: dict = {}, success: bool = True, code: int = None):
    message = "success" if success else "error"
    
    if code == None:
        code = 200 if success else 400
    
    response = make_response({"message": message, "data": content})
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.status_code = code
    
    for header in headers.items():
        response.headers[header]
    
    return response