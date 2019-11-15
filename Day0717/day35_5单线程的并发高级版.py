import socket
import select

client1 = socket.socket()
client1.setblocking(False)  #百度创建连接,非阻塞
try:
    client1.connect(('www.baidu.com', 80))
except BlockingIOError as e:
    pass

client2 = socket.socket()
client2.setblocking(False)   #搜狗创建连接,非阻塞
try:
    client2.connect(('www.sogou.com', 80))
except BlockingIOError as e:
    pass

client3 = socket.socket()
client3.setblocking(False)   #老男孩创建连接,非阻塞
try:
    client3.connect(('www.oldboyedu.com', 80))
except BlockingIOError as e:
    pass

socket_list = [client1,client2,client3]
conn_list = [client1,client2,client3]

while True:
    rlist,wlist,elist=select.select(socket_list,conn_list,[],0.005)
    # rlist 与 socket_list 有关,监测服务端是否给我返回数据,如果服务端返回数据则添加进 rlist 列表中
    # eg : [client1,client2]     数据返回来了     可读
    # wlist  与 conn_list 有关,监测其中的所有socket是否已经和服务端连接成功 ,连接成功的socket将被以列表格式存放在wlist中
    # eg: [client1,client2]        连接成功了    可写
    for sk in wlist:
        if sk == client1:
            sk.sendall(b'GET /s?wd=alex HTTP/1.0r\r\nhost:www.baidu.com\r\n\r\n')
        elif sk == client2:
            sk.sendall(b'GET /web?query=abc HTTP/1.0\r\nhost:www.sogou.com\r\n\r\n')
        else:
            sk.sendall(b'GET /s?wd=bc HTTP/1.0\r\nhost:www.oldboyedu.com\r\n\r\n')
        conn_list.remove(sk)
    for sk in rlist:
        chunk_list = []
        while True:
            try:
                chunk = sk.recv(8096)
                if not chunk:
                    break
                chunk_list.append(chunk)
            except BlockingIOError as e:
                break
        body = b''.join(chunk_list)
        # print(body.decode('utf-8'))
        print('--------->',body)
        sk.close()
        socket_list.remove( sk)

    if not socket_list:
        print('全部检测完成了')
        break


