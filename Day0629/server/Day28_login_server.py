import socket

sock = socket.socket()
IP_PORT = ('127.0.0.1', 8008)
sock.bind(IP_PORT)
sock.listen(5)

while True:
    conn,addr = sock.accept()
    while 1:
        #接收消息
        data = conn.recv(1024)
        print("信息是:",data.decode("utf8"))
        user,pwd = data.split("|")

        #文件操作
        flag = False
        with open("account","r") as f:
            for line in f:
                username,password = line.strip().split(":")
                print(username,password)
                if username == user and password ==pwd:
                    flag = True
                    break
        if flag:
            conn.send(b"success")
        else:
            conn.send(b"fail")
