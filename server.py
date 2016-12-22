import os
from pymongo import MongoClient

try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

#uri = "mongodb://admin:VSBVBFCGCIFGXQFS@bluemix-sandbox-dal-9-portal.0.dblayer.com:19651/admin?ssl=true"


# VCAP_SERVICES mapping Start

services = os.getenv('VCAP_SERVICES')
services_json = json.loads(services)
mongodb_url = services_json['compose-for-mongodb'][0]['admin:VSBVBFCGCIFGXQFS']['mongodb://admin:VSBVBFCGCIFGXQFS@bluemix-sandbox-dal-9-portal.0.dblayer.com:19651/admin?ssl=true']                     
#------>>>>>>> Map your vcap_services here
#connect:
client = MongoClient(mongodb_url)  
#get the default database:
db = client.get_default_database()  
print('connected to mongodb!, welcome to mongodb connection, have a fun')

# VCAP_SERVICES mapping END

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()