import socket, ssl
import sys

#Longer Runtime
#Function to receive full response
def request(s_sock):
    length_start=0
    chunk_size=4096
    data = bytes()
    chunk = bytes()
    length = length_start
    
    while True:
        try:
            chunk = s_sock.recv(4096)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
            s_sock.close()
            
        if ( len(chunk) < 1) :break
        
        flag = 0
        # Accept only 200 OK
        if("HTTP/1.1" in chunk.decode("utf-8")):
            try:
                version, status, reason, val = chunk.split(None, 3)
                if(status.decode("utf-8") == "200"):
                    data += chunk
                    length += len(chunk)
                    flag = 0
                else: 
                    flag = 1 
                    break
            except ValueError: break
        elif (flag == 0):
            data += chunk
            length += len(chunk)
            
    return data  

#Function to separate header and body
def extractor(data):
    try:
        index = data.index(b'\r\n\r\n')
    except:
        head = data
        body = bytes()
    else:
        index += len(b'\r\n\r\n')
        head = data[:index]
        body = data[index:]
    return (head,body)
        
#Function to Write body to file
def writeToFile(body,filename,contentType):
    if(contentType == "text/html"):
        filename = filename+".html"
    elif(contentType == "text/php"):
        filename = filename+".php"
#     else: filename = filename+".txt"

    with open(filename, 'w') as file:
        file.write(body.decode("utf-8"))
    
if __name__ == '__main__':
    
    sslVal = False
    url = "https://west.uni-koblenz.de/studying/ws2223/introduction-web-science"
#     url = "http://west.uni-koblenz.de/index.php"
    PATH = "/"
    
#     if len(sys.argv) == 2:
#         url = sys.argv[1] 
#     else: print("Invalid Input")

    try:
        li =url.split("/")
        HOST = li[2]
        if (len(li)>2): PATH = url.split(HOST)[1]
        if(li[0] == "https:"): sslVal = True
        filename = li[len(li)-1]
        if(sslVal == True): PORT = 443
        else: PORT = 80 
    except: 
        print("Failed")

    url = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (PATH,HOST)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if(sslVal == True): 
        s_sock = context.wrap_socket(s, server_hostname=HOST)
        s_sock.connect((HOST, PORT))
        s_sock.send(url.encode())
        data = request(s_sock)
    else: 
        s.connect((HOST, PORT))
        s.send(url.encode())
        data = request(s)

    (head,body) = extractor(data) 
    
    #Print header
    x = head.decode("utf-8")
    print(x)
    
    #Write body to file 
    d = dict()
    for y in x.split('\r\n'):
        try: 
            (a,b) = y.split(": ")
            d[a] = b
        except: contentType = ""
            
    if 'Content-Type' in d: contentType = d['Content-Type']
    writeToFile(body, filename, contentType)
        
    if(sslVal == True): s_sock.close()
    else : s.close()