import socket
import time
echoClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoClient.connect(("127.0.0.2", 32007))
read = echoClient.recv(1024).decode()
#time.sleep(1)
print("client 1 saw the number : ", read)
echoClient.send('ACK_client1'.encode())