import  socket
sock = socket.socket()
sock.connect(("127.0.0.1",8008))

while 1:
    user=input("用户名>>>")
    pwd=input("密码>>>")
    val = ("%s | %s"%(user,pwd)).encode("utf8")
    sock.send(val)
    response = sock.recv(1024)
    print(response.decode("utf-8"))
    if response.decode("utf-8")=="success":
        break
    else:
        continue

# while True:
#     name = input("请输入用户名:")
#     sock.send(name.encode('utf-8'))
#     if name == 'exit':
#         break
#     response = sock.recv(1024)
#     print(response.decode('utf-8'))
#
# sock.close()