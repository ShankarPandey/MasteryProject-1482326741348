import os
from pymongo import *

try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files

#uri = "mongodb://admin:VSBVBFCGCIFGXQFS@bluemix-sandbox-dal-9-portal.0.dblayer.com:19651/admin?ssl=true"
uri = "mongodb://admin:VSBVBFCGCIFGXQFS@bluemix-sandbox-dal-9-portal.0.dblayer.com"

client = MongoClient()

client = MongoClient(uri)
print client

db = client.LCHAnlyzer
print db

ReadData = db.Test
ReadData_bpk = ReadData.find()
for doc in ReadData_bpk:
    print doc

os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

