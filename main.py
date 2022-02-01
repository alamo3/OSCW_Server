from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import json
import cgi
import socket

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):
        pathAbs = self.path.removeprefix("/")
        pathDir = pathAbs.split("/")
        print(pathDir)
        self._set_headers()
        self.wfile.write(bytes(json.dumps({'success' : 'true'}), 'utf-8'))


    def do_PUT(self):
        pass

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype = self.headers.get_content_type()


        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        print(self.headers)

        # read the message and convert it into a python dictionary

        length = int(self.headers['Content-length'])
        message = json.loads(self.rfile.read(length))

        # add a property to the object, just to mess with data
        message['success'] = 'true'

        # send the message back
        self._set_headers()
        self.wfile.write(bytes(json.dumps(message), 'utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=52345):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    device_ip = s.getsockname()[0]

    print(device_ip)

    server_address = (device_ip, port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
