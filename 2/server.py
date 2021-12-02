import socket 
from threading import *
import time

echoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoSocket.bind(("127.0.0.2", 32007))
echoSocket.listen()
obj = Semaphore(2)


while True : 
    print("Waiting for Connection ...")
    (cl, clientAdress) = echoSocket.accept()
    print(clientAdress, cl)
    def recv():
        with open("info.txt", "r") as f:
            balance = int(f.read())
            f.close()
        obj.acquire()
        balance += int(cl.recv(1024).decode())
        with open("info.txt", 'w') as f:
            f.write(str(balance))
        time.sleep(0.5)
        obj.release()
        return
    def send():
        with open("info.txt", "r") as f:
            balance = int(f.read())
            f.close()
        obj.acquire()
        cl.send(str(balance).encode())
        time.sleep(0.5)
        obj.release()
        return
    t1 = Thread(target=recv)
    t2 = Thread(target=send)
    #t1.start()
    #t2.start()


    