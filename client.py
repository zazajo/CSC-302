import socket
import time

def run_client():
    # Server configuration (must match the server)
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Connect to the server
            print(f"Connecting to server at {HOST}:{PORT}...")
            client_socket.connect((HOST, PORT))
            
            # Send a message to the server
            message = "Hello from client!"
            print(f"Sending: {message}")
            client_socket.sendall(message.encode('utf-8'))
            
            # Receive the server's response
            data = client_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}")
            
    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_client()