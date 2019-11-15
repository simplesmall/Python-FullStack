import socket
import threading
import time

server = socket.socket()
server.bind(('127.0.0.1',8001))
server.listen(5)

def task(conn):
    data = conn.recv(1024)
    print(data)
    conn.close()

while True:
    conn,addr = server.accept()
    t = threading.Thread(target=task,args=(conn,))
    t.start()