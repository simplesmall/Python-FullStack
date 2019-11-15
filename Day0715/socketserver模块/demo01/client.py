import  socket

sk = socket.socket()

sk.connect(('10.10.10.174',8899))

while 1:
    name = input(">>>>>:")
    sk.send(name.encode('utf-8'))

    response = sk.recv(1024)
    print(response.decode('utf-8'))