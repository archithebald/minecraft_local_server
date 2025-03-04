import os

from flask import make_response

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

ROOT = os.getcwd()

SERVERS = os.path.join(ROOT, "servers")
ROUTES = os.path.join(ROOT, "routes")

MODELS = os.path.join(ROOT, "models").split("\\")[-1]