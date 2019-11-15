from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import pymysql


def application(environ, start_response):
    '''
    :param environ:所有的请求
    :param start_response: 封装数据请求的方法
    :return:
    '''
    print("environ", environ)
    print("PATH_INFO", environ.get("PATH_INFO"))
    path = environ.get("PATH_INFO")
    data = b"404!"
    if path == "/login":
        with open("login.html", "rb") as f:
            data = f.read()
    elif path == "/auth":
        # 登录认证

        # 1 获取用户输入的用户名和密码
        # 得到输入的字符长度
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        # 根据长度从input中读取出要用的那部分
        request_body = environ['wsgi.input'].read(request_body_size)
        print("==========>",request_body)  # ==========> b'user=asd&pwd=1234'
        data = parse_qs(request_body)       #将字符串生成字典类型
        user = data.get(b"user")[0].decode("utf8")   #取出字典数组中的第一个元素,并将编码从b"xxx"改为 xxx
        pwd = data.get(b"pwd")[0].decode("utf8")
        # 2 数据库校验,查看提交用户是否合法
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            db='web'
        )
        cur = conn.cursor()
        SQL = "select * from userinfo where name ='%s' and password ='%s'" % (user, pwd)
        cur.execute(SQL)
        # 3 响应
        if cur.fetchone():
            data = "Login successful".encode("utf8")
        else:
            data = "Login failed".encode("utf8")
        # data="提交成功!".encode("gbk")
    start_response('200  OK', [('Content-Type', 'text/html'), ("K1", "V1")])
    return [data]


httpd = make_server('', 8080, application)

print('Serving HTTP on port 8080... ')

# 开始监听HTTP请求
httpd.serve_forever()
