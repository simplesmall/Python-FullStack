import socket

# 创建socket对象
server = socket.socket()

# server.bind(('127.0.0.1', 9999))
server.bind(('10.10.10.174', 9999))
#后面可以等五个人
server.listen(5)

#等待客户端连接
#conn是客户端和服务端连接的对象(伞),服务端以后要通过该对象进行数据收发
#addr是客户端的地址信息
conn,addr = server.accept()
print(12123)

print('有人来连接了',conn,addr)
#一次最多收发的字节数
#
data = conn.recv(1024)
print(data)

#服务端给客户端回复消息
conn.send(b'stop')
#
# conn.close()