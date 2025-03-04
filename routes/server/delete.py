import os

from flask import request

from utils.database import Database
from utils.server_methods import send_response
from utils.files import delete_folder
from utils.config import SERVERS

def route():
    db = Database()
    
    server_id = request.args.get("id")
    
    return db.safe_delete_server(server_id)