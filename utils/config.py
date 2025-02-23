import os

ROOT = os.getcwd()

SERVERS = os.path.join(ROOT, "servers")

SCRIPTS = os.path.join(ROOT, "scripts")
START_SCRIPT = os.path.join(SCRIPTS, "start.bat")

def server_exists(server_id):
    return os.path.exists(os.path.join(SERVERS, server_id))