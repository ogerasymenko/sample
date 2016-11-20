import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://192.168.10.109:6789/")
path = "/tmp/Test_Folder/"

result = proxy.list_dir(path)
print(result)
