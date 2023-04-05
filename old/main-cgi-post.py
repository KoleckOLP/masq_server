import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 80  # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on port {PORT}...")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)  # Receive data from the client
            if data:
                # Find the end of the HTTP header
                header_end = data.find(b"\r\n\r\n")
                if header_end != -1:
                    # Parse the HTTP header
                    header = data[:header_end].decode("utf-8")
                    method, path, _ = header.split("\r\n")[0].split(" ")
                    if method == "POST":
                        # Get the length of the POST data
                        content_length = int(header.split("Content-Length: ")[1].split("\r\n")[0])
                        # Get the POST data from the request
                        post_data = data[header_end+4:header_end+4+content_length]
                        print(f"Received POST data: {post_data.decode('utf-8')}")
                        # Do something with the POST data here...
                        # For example, you could parse it into a dictionary using the `urllib.parse` module
                        # and then use the data to generate a response.
                        response_data = "Hello, World!"
                        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_data)}\r\n\r\n{response_data}"
                        conn.sendall(response.encode('utf-8'))
                        conn.close()
                        break
            conn.close()