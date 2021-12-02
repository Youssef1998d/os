import socket 
echoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoSocket.bind(("127.0.0.2", 32007))
echoSocket.listen()
while True:
    (cl, clientAdress) = echoSocket.accept()

    with open("info.txt", "r") as f:
        balance = str(f.read())
        f.close()
        cl.send(balance.encode())

        print(balance, ' sent to last connection\n')
    read = cl.recv(1024).decode()
    if read.isdigit() and balance != "":
        with open("info.txt", "w") as f:
            f.write(str(int(balance)+(int(read))))
            f.close()
        cl.send(("ACK_MODIF_client2").encode())
    else:
        print(read)
        break
        