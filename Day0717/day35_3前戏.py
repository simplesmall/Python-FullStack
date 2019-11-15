import socket

client = socket.socket()
# client.setblocking(False)  #将原来阻塞的位置变成非阻塞(报错)
try:
    client.connect(('www.baidu.com', 80))
except BlockingIOError as e:
    pass

client.sendall(b'GET /s?wd=bilibili HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
chunk_list = []
while True:
    try:
        chunk = client.recv(8096)
    except BlockingIOError:
        pass
    if not chunk:
        break
    chunk_list.append(chunk)
body = b''.join(chunk_list)
print(body.decode('utf-8'))
