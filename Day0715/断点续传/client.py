import os
import socket
import json
import hashlib

CODE = {
    '1001': '上传文件,从头开始上传'
}


def file_md5(file_path):
    """
    对文件进行MD5加密
    :param file_path:
    :return:
    """
    obj = open(file_path, 'rb')
    m = hashlib.md5()
    for line in obj:
        m.update(line)
    return m.hexdigest()


sk = socket.socket()

sk.connect(("127.0.0.1", 8001))

while True:
    cmd = input("请输入要执行的命令")
    """
    1.自定义协议,按照自定义协议的规则来收发数据
    """
    file_path = "111.jpg"
    file_md5_val = file_md5(file_path)
    file_name = os.path.basename(file_path)
    file_size = os.stat(file_path).st_size

    cmd_dict = {'cmd': 'upload', 'file_name': file_name, 'size': file_size, 'md5': file_md5_val}
    upload_cmd_bytes = json.dumps(cmd_dict).encode('utf-8')
    sk.sendall(upload_cmd_bytes)
    """
    2.等待服务端的响应
    """
    response = json.loads(sk.recv(8096).decode('utf-8'))
    if response['code'] == 1001:
        # 从头开始:文件迭代
        """
        with open(file_path, mode='rb')as f:
            for line in f:
                sk.sendall(line)
        """
        f = open(file_path, mode='rb')
        send_size = 0
        while send_size < file_size:
            data = f.read(1024)
            sk.sendall(data)
            send_size += len(data)
        f.close()
        print("上传成功")
    else:
        # 断点续传
        exit_size = response['size']
        f = open(file_path,'rb')
        f.seek(exit_size)
        while send_size<file_size:
            data = f.read(1024)
            sk.sendall(data)
            send_size+=len(data)
        f.close()
        print('上传成功')
