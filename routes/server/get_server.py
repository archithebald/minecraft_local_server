from flask import request

def route(self):
    server_id = request.args.get("id")
    server = self.db.get_server(server_id=server_id)
    return self.send_response(content=server)