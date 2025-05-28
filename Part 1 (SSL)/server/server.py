import ssl
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

os.environ['SSLKEYLOGFILE'] = os.path.expanduser('log/sslkeys.log')

server_address = ('0.0.0.0', 4443)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.load_verify_locations(cafile="rootCA.pem")
context.verify_mode = ssl.CERT_REQUIRED

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Server running on https://192.168.179.147:4443")
httpd.serve_forever()
