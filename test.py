from server import Server
from utils.database import Database
import time

db = Database()
server_id = "67b78cb214f2889f2c78e9e0"
s = Server(server_db=db.get_server(server_id), server_id=server_id)
s.start()

time.sleep(13)

s.send_command("op gaialoki08")

time.sleep(100)