import  socket

client = socket.socket()

client.sendall(b'GET /s?wd=bilibili HTTP/1.0\r\nhost:www.tcig.cn\r\n\r\n')
chunk_list =[]
while True:
    try:
        chunk = client.recv(8096)
    except BlockingIOError:
        pass
    if not chunk:
        break
    chunk_list.append(chunk)
body = b''.join(chunk_list)
print(body)
