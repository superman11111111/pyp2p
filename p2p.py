import socket
import sys
import time
import threading
from settings import *


def connect():
    global IP, PORT
    socket_established = 0
    while not socket_established:
        try:
            sendingsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sendingsock.connect((IP, PORT))
            socket_established = 1
            break
        except Exception as e:
            print(e)
            sendingsock.close()
            print(f"Cannot establish send socket - retrying in {RETRY_DELAY}")
            time.sleep(RETRY_DELAY)
    # print(socket.getsockname()[0])
    print(f"Sending socket established, ip:{IP} port:{PORT}")
    sendingsock.send(b"hello world!")
    while 1:
        sendingsock.send(input().encode())


def listen():
    global PORT
    socket_failure = 1
    while socket_failure:
        try:
            serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            serversock.bind(("127.0.0.1", PORT))
            serversock.listen(5)
            socket_failure = 0
            print(f"Listening socket established port:{PORT}")
            break;
        except Exception as e:
            print(e)
            serversock.close()
            print(f"Cannot establish listening socket - retrying in {RETRY_DELAY}")
            time.sleep(RETRY_DELAY)
    while 1:
        print("Waiting for incoming traffic")
        (clientsock, address) = serversock.accept()
        print(clientsock, address)
        while clientsock.fileno() != -1:
            recv = clientsock.recv(2048)
            if recv:
                print(recv)
if len(sys.argv) > 3:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    if sys.argv[3] == "listen":
        listen_t = threading.Thread(target=listen, args=())
        listen_t.start()
        listen_t.join()
        quit()
    if sys.argv[3] == "send":
        connect_t = threading.Thread(target=connect)
        connect_t.start()
        connect_t.join()
        quit()
        

if len(sys.argv) > 2:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])

print(f"IP={IP} PORT={PORT}")


listen_t = threading.Thread(target=listen, args=())
listen_t.start()
connect_t = threading.Thread(target=connect)
connect_t.start()
listen_t.join()
connect_t.join()



