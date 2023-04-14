# got the TCP connection, does not do post.

import socket

HOST = "192.168.2.60"
PORT = 80

print(f"started socket on {HOST}:{PORT}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print(data)
                #break
            conn.sendall(data)
