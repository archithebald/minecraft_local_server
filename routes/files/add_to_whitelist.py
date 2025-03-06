import os, json

from flask import request

from utils.config import SERVERS, send_response

def route():
    server_id = request.args.get("id")
    usernames = [str(username) for username in request.args.get("usernames").split(",")]
    
    path = os.path.join(SERVERS, server_id)
    
    f = open(os.path.join(path, "whitelist.json"), "w", encoding="utf-8")
    json.dump(usernames, f)
    
    return send_response()