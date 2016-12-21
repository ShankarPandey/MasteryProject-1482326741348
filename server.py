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

name = "bmix_dal_yp_894e58c3_c77e_4c0f_972c_bbc6d91f2733"
#uri_cli = "mongo --ssl --sslAllowInvalidCertificates bluemix-sandbox-dal-9-portal.4.dblayer.com:20712/admin -u admin -p EJMSKZJPETYIWCCK"
uri = "mongodb://admin:EJMSKZJPETYIWCCK@bluemix-sandbox-dal-9-portal.4.dblayer.com:20712,bluemix-sandbox-dal-9-portal.0.dblayer.com:20712/admin?ssl=true"

client = MongoClient()

client = MongoClient(uri)
print client

db = client.Prototypes
print db

ReadData = db.Data_train_bpk
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

