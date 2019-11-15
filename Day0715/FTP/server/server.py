import socket
import  json

sock = socket.socket()
sock.bind(('10.10.10.174',8800))

# 最大排队数
sock.listen(5)

while 1:
    print("server is working....")
    conn,addr = sock.accept()

    while 1:
        file_info_json=conn.recv(1024).decode("utf-8")
        file_info = json.loads(file_info_json)
        print("file_info",file_info)

        #文件信息
        action = file_info.get('action')
        filename = file_info.get('filename')
        filesize = file_info.get('filesize')

        conn.send(b"200")

        #接收文件数据
        with open("put/"+filename,"wb") as f:
            recv_data_length = 0
            while recv_data_length>filesize:
                data = conn.recv(1024)
                recv_data_length+=len(data)
                f.write(data)
                print("文件大小:%s,已成功接收%s"%(filesize,recv_data_length))