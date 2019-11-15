import os
import socket
import  json

sock = socket.socket()
sock.connect(('10.10.10.174',8800))

while 1:
    cmd = input("请输入命令: ") # put  111.jpg

    action,filename=cmd.strip().split(" ")
    filesize=os.path.getsize(filename)

    file_info={
        "action",action,
        "filename",filename,
        "filesize",filesize,
    }
    file_info_json = json.dumps(file_info).encode("utf-8")
    sock.send(file_info_json)

    #确认服务端接收到了文件信息
    code = sock.recv(1024).decode("utf-8")

    if code =="200":
        with open(filename,"rb") as f:
            for line in f:
                sock.send(line)
    else:
        print("服务器异常!")
