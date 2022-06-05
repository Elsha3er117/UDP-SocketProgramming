from socket import *
import sys
serverIP = '127.0.0.1'
serverPort=int(sys.argv[1])

clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.bind(('',serverPort))

message = " ".join(sys.argv[2::])
clientSocket.sendto(message.encode(), (serverIP,12000))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (f"Message : {modifiedMessage.decode()} ")

clientSocket.close()
