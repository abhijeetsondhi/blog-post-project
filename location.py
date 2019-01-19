import urllib.request
import socket
import json
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
url='http://ip-api.com/json/'+ IPAddr
req = urllib.request.Request(url)
out = urllib.request.urlopen(req).read()
jsonres = json.loads(out.decode('utf-8'))
print(jsonres['city'])
