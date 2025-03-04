import os, requests

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
    
def download_file(url: str, path_to_download: str, file_name: str, extension: str):
    response = requests.get(url=url, stream=True)
    
    if response.status_code == 200:
        try:
            with open(os.path.join(path_to_download, file_name+"."+extension), "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
                print(f">>> Download at: {path_to_download} ✅")
        except PermissionError as e:
            print("Please allow permissions.")
            return None
    else:
        print(f">>> Failed to download {path_to_download}. Status code: {response.status_code} ❌")
        
def remove_file(path: str): # TODO
    pass