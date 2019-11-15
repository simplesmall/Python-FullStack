import requests
from bs4 import BeautifulSoup

r1=requests.get(
    url='https://dig.chouti.com/',
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
)
# print(r1.content)
# print(r1.text)
#查看下载下来的文件
soup = BeautifulSoup(r1.text,'html.parser')
content_list = soup.find('div',attrs={'id':'content-list'})
for child in content_list.children:
    print('----------',child)