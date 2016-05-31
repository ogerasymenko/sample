import os, sys, re

log_file = "/var/log/nginx/access.log"

def get_cwd():
    print("{0:.<25} {1}" .format("Current directory:", os.getcwd()))
    print("{0:.<25} {1}" .format("Python file:", os.path.abspath(__file__)))
    print("{0:.<25} {1}" .format("Reading file:", os.path.abspath(log_file)))

def print_error():
    print("Cannot read the file")
    print("Please check, what file exists and have 'read' permission for 'other' group")

c = get_cwd()
print()

ip_regex = re.compile(r"\b([0-9]{1,3}\.){3}[0-9]{1,3}\b")

s = set()

file_s = open(log_file)

try:
    for line in file_s:
        a = re.search(ip_regex, line)
        b = a.group()
        s.add(b)
        
    arr = list(s)
    arr.sort()

    for i in arr:
        print(i)
        
    print()     
    print("Total quantity of unique IP-addresses is", len(arr), "pcs.")

except (IsADirectoryError, FileNotFoundError, PermissionError):
    print_error()

finally:
    file_s.close()

