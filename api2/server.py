import socket

HOST = '0.0.0.0'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[API2] Listening on {PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[API2] Connected by {addr}")
            data = conn.recv(1024)
            if data:
                http_response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    "Content-Length: 14\r\n" # Set content-length to 14 bytes because "PONG from API2" is only 14 bytes
                    "\r\n"
                    "PONG from API2" 
                )
                conn.sendall(http_response.encode())
