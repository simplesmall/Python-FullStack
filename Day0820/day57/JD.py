import socket


def handle_request(client):
    request_data = client.recv(1024)
    print("request_data:", request_data)
    # client.send("HTTP/1.1  200 OK\r\n status: 200 \r\n Content-Type:text/html \r\n\r\n<h1>Hello world</h1><image url='https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2925061987,411404233&fm=26&gp=0.jpg'>".encode("utf8"))
    with open("login.html", "rb") as f:
        data = f.read()
    client.send(b"HTTP/1.1  200 OK\r\n status: 200 \r\n Content-Type:text/html \r\n\r\n" + data)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8812))
    sock.listen(5)

    while True:
        print("The server is waiting for client-connecting...")
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
