import os

from utils.config import SERVERS, ROOT

def get_server_folder(server_id: str):
    server_path = os.path.join(SERVERS, server_id)
    
    if not os.path.exists(server_path):
        return None
    
    return server_path

def get_server_files(server_id: str):
    data = {}
    
    path = os.path.join(SERVERS, server_id)
    root = path.split("\\")[-1]
    
    for dirpath, _, filesnames in os.walk(path):
        files = {}
        
        for file in filesnames:
            files[file] = {"size": os.path.getsize(os.path.join(dirpath, file))}
        
        data[dirpath.split(root, 1)[-1].removeprefix("\\")] = {"type": "dir", "files": files}
        
    return data

def get_server_file_path(server_id: str, path: str, name: str):
    return os.path.join(SERVERS, server_id, path, name)

def read_file_content(path: str, server_id: str):
    f = open(os.path.join(SERVERS, server_id, path), "r", encoding="utf-8")
    
    try:
        content = f.read()
        
        return content
    except Exception as e:
        return None