# Import http.server and socketserver modules
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

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
        # Check if the request is a cgi post request
        if self.path.startswith('/cgi-bin/'):
            # Send a 200 OK response
            self.send_response(200)

            # Open a file and read it's data as bytes
            with open('test2.gif', 'rb') as f:
                image_data = f.read()

            # Send headers
            self.send_header('Content-type', 'image/gif')  # image/gif, text/plain
            self.send_header('Content-Length', len(image_data))
            self.end_headers()

            # Write some content to the response
            self.wfile.write(image_data)
            # self.wfile.write(b'Hello from python!')
            
            # Read the request data
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)

            # Decode and print the request data
            data = data.decode('utf-8')
            print(data)

# Define the port on which you want to run the server
host = "192.168.2.60"
port = 80

# Create a server object using the handler class, host ip and port number
server = HTTPServer((host, port), MyHandler)

# Print a message to indicate that the server is running
print(f'Server running on port {port}')

# Serve forever
server.serve_forever()
