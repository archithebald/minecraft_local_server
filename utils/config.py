import os

from flask import make_response

ROOT = os.getcwd()

SERVERS = os.path.join(ROOT, "servers")
ROUTES = os.path.join(ROOT, "routes")

def server_exists(server_id):
    return os.path.exists(os.path.join(SERVERS, server_id))

def send_response(content: str = ""):
    response = make_response({"message": "success", "data": content})
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response