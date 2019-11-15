import os
import socketserver
import json
import shutil

CODE = {
    '1001': '上传文件,从头开始上传'
}


class NBServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        self.request  是客户端的socket对象
        :return:
        """
        # 1.接收命令
        upload_cmd_bytes = self.request.recv(8096)
        cmd_dict = json.loads(upload_cmd_bytes.decode('uutf-8'))
        print(cmd_dict)
        # 2.获取文件信息
        file_md5 = cmd_dict['md5']
        file_name = cmd_dict['file_name']

        file_md5_path = os.path.join('home', 'zhangyu', file_md5)
        file_name_path = os.path.join('home', 'zhangyu', file_name)
        upload_file_size = cmd_dict['size']
        # 3.判断文件是否存在
        exist = os.path.exists(file_md5_path)
        # 尽量简单的代码往上写
        if not exist:  # 续传
            # 3.1.1 可以开始上传了,我已经准备好
            exist_size = os.stat(file_name_path).st_size
            response = {'code': 1001}
            self.request.sendall(json.dumps(response).encode('utf-8'))
            #应该是追加而不是写覆盖掉
            f = open(file_md5_path, 'ab')

            #3.1.2 接收上传的文件内容
            recv_size = exist_size
            while recv_size < upload_file_size:
                data = self.request.recv(1024)
                f.write(data)
                f.flush()
                recv_size += len(data)
            f.close()
            #3.1.3 改名字
            # os.rename('a','b')
            if not os.path.exists(file_name_path):
                shutil.move(file_md5_path,file_name_path)
            else:
                while True:
                    pass


        else:  # 不续传
            # 3.2 续传 + 大小
            exist_size = os.stat(file_md5_path).st_size
            response = {'code': 1002, 'size': exist_size}
            self.request.sendall(json.dumps(response).encode('utf-8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), NBServer)
    server.serve_forever()
