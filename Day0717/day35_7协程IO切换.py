from gevent import monkey
monkey.patch_all()  #以后代码中遇到ID都会自动执行greenlet 的 switch进行切换
import requests

import gevent

def get_page(url):
    ret = requests.get(url)
    print(url,ret.content)

gevent.joinall([
    gevent.spawn(get_page,'http://www.python.org'),
    gevent.spawn(get_page,'http://www.yahoo.com'),
    gevent.spawn(get_page,'http://www.github.com'),
])