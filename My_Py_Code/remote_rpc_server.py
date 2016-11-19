import os
from xmlrpc.server import SimpleXMLRPCServer


def list_dir(path):
    # print("Removing files ", os.listdir(path))
    for (path, dir, file) in os.walk(path):
        for file_name in file:
            os.remove(os.path.join(path, file_name))
    return "Done"

server = SimpleXMLRPCServer(("192.168.10.109", 6789), allow_none=True)
server.register_function(list_dir, "list_dir")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print(" Interrupted by keyboard. Exit.")
