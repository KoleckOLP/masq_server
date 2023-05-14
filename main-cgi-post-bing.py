# Import http.server and socketserver modules
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from importlib import reload
import response
# import socketserver

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

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
            # Read the request data
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)

            # Decode and print the request data
            data = data.decode('utf-8')
            print(data)

            # Send a 200 OK response
            self.send_response(200)

            ## Here is implemented everything that gamstat figured out on reddit
            if "checkmessages" in data:
                print("checkmessages")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b'["messagetext": ["cost": "this is cost", "more": "this is more", "license": "this is license", "emailtext": "this is emailtext", "warnpages": "warnpages"]]'
            elif "createuserid" in data:
                print("createuserid")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b'["userID": "123"]'
            elif "saveother" in data:
                print("saveother")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b''  # yep just empty reply, but I still send headder
            elif "firsttimeprojector" in data:
                print("firsttimeprojector")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b'["messagetext": [""]]'
            elif "getlasthistory" in data:
                print("getlasthistory")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b'["lasthistory": ""]'
            elif "getticketsleft" in data:
                print("getticketsleft")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b'["ticketsleft": 66]'
            elif "createusername" in data:
                print("getticketsleft")
                self.send_header('Content-type', "plain/text")
                self.end_headers()
                return_data = b'["userName": "namefromreply"]'
            else:
                print("!!! unimplemented !!!")
                try:
                    reload(response)
                    contentype, return_data = response.give_data()
                except Exception as e:
                    print(e)
                ## Here is implemented my dynamic testing
                # Send headers
                self.send_header('Content-type', contentype)  # image/gif, text/plain
                # self.send_header('Content-Length', len(image_data))
                self.end_headers()

            # Write some content to the response
            # self.wfile.write(image_data)
            self.wfile.write(return_data)
            print(str(return_data)+"\n")

local_ip = get_local_ip()

# Define the port on which you want to run the server
host = local_ip
port = 80

# Create a server object using the handler class, host ip and port number
server = HTTPServer((host, port), MyHandler)

# Print a message to indicate that the server is running
print(f'Server running on port {host}:{port}')

# Serve forever
server.serve_forever()
