import socket
echoClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoClient.connect(("127.0.0.2", 32007))
read = echoClient.recv(1024).decode()
print("client 2 saw the number : ", read)
echoClient.send((input("add the amount to the number : ").encode()))
print(echoClient.recv(1024).decode())