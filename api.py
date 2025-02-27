import os, importlib

from utils.config import ROUTES
from flask import Flask

class API:
    def __init__(self):
        self.app = Flask(import_name=__name__)
        
        self.routes()

    def routes(self):
        for root, _, files in os.walk(ROUTES):
            for file in files:
                if file.endswith(".py"):
                    name = file.split(".")[0]
                    relative_folder = os.path.relpath(root, ROUTES).replace(os.sep, ".")
                    
                    module_name = ""
                
                    if relative_folder == ".":
                        module_name = name
                    else:
                        module_name = f"{relative_folder}.{name}"
                        
                    module = importlib.import_module(name=f"routes.{module_name}")
                    
                    if name == "index":
                        self.app.add_url_rule(f"/", name, module.route)
                    else:
                        self.app.add_url_rule(f"/{name}", name, module.route)
        
    def run(self):
        self.app.run(host="0.0.0.0")