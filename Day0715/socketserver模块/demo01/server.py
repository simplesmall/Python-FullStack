import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            try:
                print("等待信息")
                data = self.recv(1024)
                if len(data) ==0:
                    break
                if data == b'exit':
                    break
                response = data + b'SB'
                self.send(response)
            except Exception as e:
                break
        # self.close()

server=socketserver.ThreadingTCPServer(('10.10.10.174',8899),Myserver)
server.serve_forever()