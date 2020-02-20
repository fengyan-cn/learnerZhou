from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>>')
    if not data:
        break
    tcpCliSock.send(str.encode(data))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()