import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://192.168.10.109:6789/")
path = "/tmp/Test_Folder/"

proxy.list_dir(path)
