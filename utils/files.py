import os, requests, shutil

from utils.config import SERVERS, ROOT, send_response

readable_extensions = [
    "txt", "md", "csv", "json", "xml", "yaml", "yml", "html", "htm",
    "css", "js", "ts", "py", "java", "c", "cpp", "h", "cs", "php",
    "rb", "go", "swift", "kt", "rs", "sh", "bat", "sql", "r", "pl",
    "tex", "rst", "docx", "odt", "rtf", "pdf",
    "ini", "cfg", "toml", "log", "env", "properties",
    "ipynb", "rmd", "ps1",
    "svg", "vbs", "lua", "asm", "tsv"
]

def get_server_folder(server_id: str):
    server_path = os.path.join(SERVERS, server_id)
    
    if not os.path.exists(server_path):
        return None
    
    return server_path

def get_server_files(server_id: str):
    data = {}
    
    path = os.path.join(SERVERS, server_id)
    root = path.split("\\")[-1]
    
    for dirpath, dirnames, filesnames in os.walk(path):
        files = []
        
        for file in filesnames:
            can_read = True if file.split(".")[-1] in readable_extensions else False
            files.append({"name": file, "type": "file", "size": os.path.getsize(os.path.join(dirpath, file)), "can_read": can_read})
        
        for dirname in dirnames:
            files.append({"name": dirname, "type": "dir", "size": os.path.getsize(os.path.join(dirpath, dirname))})
        
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
                return True
        except PermissionError as e:
            print("Please allow permissions.")
            return None
    else:
        print(f">>> Failed to download {path_to_download}. Status code: {response.status_code} ❌")
        return None
        
def delete_file(path: str):
    os.remove(path)