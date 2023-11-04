import socket
import json

message = {
    'scheme': 'https',  
    'host': 'www.facebook.com', 
    'port': 443,  
    'path': 'photo.php',
    'query': 'fbid=2068026323275211&set=a.269104153167446&type=3&theater',
    'fragment': '1efh3', 
} 


def client_program():
    host = socket.gethostname()  
    port = 5001  

    
    data = json.dumps(message)
    client_socket = socket.socket()  

    try:
        
        client_socket.connect((host, port))  
        client_socket.send(data.encode())

        received = client_socket.recv(1024)
        received = received.decode("utf-8")
   
    finally:
        client_socket.close()


    print("Connection Closed.!")

if __name__ == '__main__':
    client_program()