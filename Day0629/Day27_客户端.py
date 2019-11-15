import socket
client = socket.socket()
#发起连接请求
# client.connect(('127.0.0.1', 9999))
client.connect(('10.10.10.174', 9999))

#发送消息
client.send(b'hello')

#等待接收消息
data = client.recv(1024)
print(data)

client.close()