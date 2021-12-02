def seeBalance():
    import socket
    import time
    echoClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    echoClient.connect(("127.0.0.2", 32007))
    read = echoClient.recv(1024).decode()
    time.sleep(0.1)
    if not read:
        return
    print("Your Balance", read)
    echoClient.close()
    return

seeBalance()