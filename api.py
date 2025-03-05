import os, importlib

from utils.config import ROUTES, MODELS
from utils.server_methods import send_response
from models import *
from flask import Flask, request
from functools import wraps
from marshmallow import ValidationError

class API:
    def __init__(self):
        self.app = Flask(import_name=__name__)
        
        self.routes()

    def get_model_class(self, folder: str, name: str):
        model_name = f"{MODELS}.{folder}"
        model = importlib.import_module(model_name)
        
        try:
            return model.__dict__[name.upper()]
        except KeyError:
            return None

    def create_route(self, name, module_name, folder_name):
        module = importlib.import_module(f"routes.{module_name}")
        c = self.get_model_class(folder=folder_name, name=name)

        @wraps(module.route)
        def dynamic_route():
            try:
                if c != None:  
                    c().load(request.args.to_dict())
            except ValidationError as err:
                return send_response(content=f"You missed some parameters" ,success=False, code=400, error=str(err))
            try:
                return module.route()
            except Exception as e:
                return send_response(content="An error occured", success=False, code=500, error=str(e))

        dynamic_route.__name__ = name 

        self.app.route(f"/{name}")(dynamic_route)

    def routes(self):
        for root, _, files in os.walk(ROUTES):
            for file in files:
                if file.endswith(".py"):
                    name = file.split(".")[0]
                    folder_name = root.split("\\")[-1]
                    
                    relative_folder = os.path.relpath(root, ROUTES).replace(os.sep, ".")
                    
                    module_name = ""
                
                    if relative_folder == ".":
                        module_name = name
                    else:
                        module_name = f"{relative_folder}.{name}"
                                            
                    self.create_route(name=name, module_name=module_name, folder_name=folder_name)
        
    def run(self):
        self.app.run(host="0.0.0.0")