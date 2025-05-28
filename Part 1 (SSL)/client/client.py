# client

import ssl, socket

hostname = '192.168.179.147'
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='rootCA.pem')
context.load_cert_chain(certfile="client.crt", keyfile="client.key")

with socket.create_connection((hostname, 4443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:

        request = "GET / HTTP/1.1\r\nHost: 192.168.179.147\r\n\r\n"
        ssock.send(request.encode())

        response = ssock.recv(4096)
        print(response.decode())
