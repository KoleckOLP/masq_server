# Import statements
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from importlib import reload
import urllib.parse
import response

# Code I found online to get your local ip
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Define a custom handler class that inherits from BaseHTTPRequestHandler
class MyHandler(BaseHTTPRequestHandler):
    # Override the do_POST method to handle POST requests
    def do_POST(self):        
        # Check if the request is a cgi post request
        if self.path.startswith('/cgi-bin/'):
            # Read the request data
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            params = urllib.parse.parse_qs(data.decode())

            # Decode and print the request data
            data = data.decode('utf-8')
            print(data)

            # Send a 200 OK response
            self.send_response(200)

            ## Varibales to and from the game
            userID = 1
            ticketsleft = 15

            ## Here is implemented everything that gamstat figured out on reddit
            if "checkmessages" in data:
                print("checkmessages")
                contentype = "plain/text"
                # I don't like how much stuff is send using this one, I think it should be impoved (this is gamstat's super testing one)
                return_data = b'["messagetext": ["cost": "this is cost", ' \
                                               b'"more": "this is more", ' \
                                               b'"license": "Welcome to MASQ!\nYou are using a custom local server made by koleq with help of gamstat.\nIf you find any issues report them here: https://github.com/KoleckOLP/masq_server/issues\nHave fun playing MASQ!", ' \
                                               b'"emailtext": "Feel free to input nonsense data\nbut I recomend saving at the next step.", ' \
                                               b'"optionmessage": "this is option", ' \
                                               b'"firstendmessage": "firstend", ' \
                                               b'"nextendmessage": "nextend", ' \
                                               b'"return": "return", ' \
                                               b'"ZStartAgain2": "zstart", ' \
                                               b'"privacypolicy": "my privacy policy", ' \
                                               b'"emailrequired": "email required", ' \
                                               b'"episode": 5, ' \
                                               b'"messageid": "asdasdasd", ' \
                                               b'"hijack": "hijack", ' \
                                               b'"flag": "flag", ' \
                                               b'"RegisterDriven": "RegisterDriven", ' \
                                               b'"VIPpassword": "VIPpassword", ' \
                                               b'"warnpages": "warnpages", ' \
                                               b'"episodemessage": "episodemessage", ' \
                                               b'"substract": "substract", ' \
                                               b'"substractmessage": "substractmessage"]]'
            elif "createuserid" in data:
                print("createuserid")
                contentype = "plain/text"
                return_data = bytes(f'["userID": {userID}]', "ascii")  # b'["userID": "123"]'
            elif "saveother" in data:
                print("saveother")
                contentype = "plain/text"
                return_data = b''  # yep just empty reply, but I still send headder (gamnstat)
            elif "firsttimeprojector" in data:
                print("firsttimeprojector")
                contentype = "plain/text"
                return_data = b'["messagetext": [""]]'
            elif "createusername" in data:
                print("createusername")
                username = params.get("username", [""])[0]
                contentype = "plain/text"
                return_data = bytes(f'["userID": {userID}, ' \
                                    f'"userName": "{username}"]', "ascii")  # I assume you also send it userID  
            elif "getticketsleft" in data:
                print("getticketsleft")
                contentype = "plain/text"
                return_data = bytes(f'["ticketsleft": {ticketsleft}]', "ascii")
            elif "getlasthistory" in data:
                print("getlasthistory")
                contentype = "plain/text"
                return_data = b'["lasthistory": ""]'
            elif "checkcontinue" in data:
                print("checkcontinue")
                contentype = "plain/text"
                return_data = b'["messageid": "success"]'
            ## Here is implemented my dynamic testing
            else:
                print("!!! unimplemented !!!")
                try:
                    reload(response)
                    contentype, return_data = response.give_data()
                except Exception as e:
                    print(e)
                
            # Send headers
            self.send_header('Content-type', contentype)  # image/gif, text/plain
            self.end_headers()
            # Write some content to the response
            self.wfile.write(return_data)
            print(str(return_data)+"\n")

local_ip = get_local_ip()

# Define ip and the port on which you want to run the server
host = local_ip
port = 80

# Create a server object using the handler class, host ip and port number
server = HTTPServer((host, port), MyHandler)

# Print a message to indicate that the server is running
print(f'Server running on port {host}:{port}')

# Run server in a loop
server.serve_forever()
