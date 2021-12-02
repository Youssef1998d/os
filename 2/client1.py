def addBalance(v):
    import socket
    echoClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    echoClient.connect(("127.0.0.2",32007))
    echoClient.send(str(v).encode())
    echoClient.close()
    return

addBalance(150)