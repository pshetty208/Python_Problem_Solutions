import socket
import json

def server_program():
    host = socket.gethostname()
    port = 5001 

    server_socket = socket.socket()  
    
    server_socket.bind((host, port)) 

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    data = conn.recv(1024)
    data = data.decode('utf-8')
    data = json.loads(data)

    
    url = str(data['scheme']) + '://' + str(data['host']) + ':' + str(data['port']) + '/' + str(data['path']) + '?' + str(data['query']) + '#' + str(data['fragment']) 
    print("from Client: ",url)   
    conn.close()  

if __name__ == '__main__':
    server_program()