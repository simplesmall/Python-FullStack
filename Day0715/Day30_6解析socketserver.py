import socketserver
import threading
import time

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        pass
server = socketserver.ThreadingTCPServer(('10.10.10.174',8001,),Myserver)
server.serve_forever()

def task(conn):
    data = conn.recv(1024)
    print(data)
    conn.close()

while True:
    conn,addr = server.accept()
    t = threading.Thread(target=task,args=(conn,))
    t.start()