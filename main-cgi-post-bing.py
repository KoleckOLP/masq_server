# Import http.server and socketserver modules
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from importlib import reload
import response
# import socketserver

# Define a custom handler class that inherits from BaseHTTPRequestHandler
class MyHandler(BaseHTTPRequestHandler):

    # Override the do_GET method to handle GET requests (not used)
    def do_GET(self):
        # Send a 200 OK response
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write some content to the response
        self.wfile.write(b'<html><body><h1>Hello from python!</h1></body></html>')

    # Override the do_POST method to handle POST requests
    def do_POST(self):

        try:
            reload(response)
            contentype, return_data = response.give_data()
        except Exception as e:
            print(e)
        
        # Check if the request is a cgi post request
        if self.path.startswith('/cgi-bin/'):
            # Read the request data
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)

            # Decode and print the request data
            data = data.decode('utf-8')
            print(data)

            # Send a 200 OK response
            self.send_response(200)

            # Open a file and read it's data as bytes
            # with open('test.gif', 'rb') as f:
                # image_data = f.read()

            if "checkmessages" in data:
                self.send_header('Content-type', "text/json")
                self.end_headers()
                self.wfile.write(b'["messagetext": ["cost": "this is cost", "more": "this is more", "license": "this is license"]]')
            else:
                # Send headers
                self.send_header('Content-type', contentype)  # image/gif, text/plain
                # self.send_header('Content-Length', len(image_data))
                self.end_headers()

                # Write some content to the response
                # self.wfile.write(image_data)
                self.wfile.write(return_data)  # {"stuff": {"cost": 1, "more": 1, "license": 1}}
            print(return_data)

# Define the port on which you want to run the server
host = response.serverip()
port = 80

# Create a server object using the handler class, host ip and port number
server = HTTPServer((host, port), MyHandler)

# Print a message to indicate that the server is running
print(f'Server running on port {host}:{port}')

# Serve forever
server.serve_forever()
