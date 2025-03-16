import socket

def run_server():
    # Server configuration
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Allow port reuse
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to the address
        server_socket.bind((HOST, PORT))
        
        # Listen for incoming connections
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")
        
        try:
            while True:
                # Accept a connection
                client_socket, client_address = server_socket.accept()
                print(f"Connected by {client_address}")
                
                with client_socket:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    
                    # Decode and print the received message
                    request = data.decode('utf-8')
                    print(f"Received request: {request}")
                    
                    # Prepare and send a response
                    response = f"Server received: '{request}'. Hello from server!"
                    client_socket.sendall(response.encode('utf-8'))
                    print("Response sent")
        except KeyboardInterrupt:
            print("Server shutting down...")

if __name__ == "__main__":
    run_server()