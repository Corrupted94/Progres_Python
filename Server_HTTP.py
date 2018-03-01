from socket import *
from threading import *
serverPort = 1249
serverSocket = socket (AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print('server ready')


def ouvrir(nom):
    res = ""
    with open (nom,"r") as f:
        for l in f:
            res = res + l
    return res
    

def handle_client(clientSocket):
    received = clientSocket.recv(4096)
    if not received :
        clientSocket.close()
    else :
        uri = received.split()[1]
        try :
            fic = ouvrir(uri[1:])
        except :
            clientSocket.sendall('HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n')
            return
        clientSocket.sendall('HTTP/1.1 200 OK\r\nCache-Control: no-cache, private\r\nContent-Length: '+str(len(fic))+'\r\nDate: Mon, 24 Nov 2014 10:21:21 GMT\r\n\r\n')
        clientSocket.sendall(fic)
        
while True :
    clientSocket, address = serverSocket.accept()
    Thread(target=handle_client, args=(clientSocket,)).start()

