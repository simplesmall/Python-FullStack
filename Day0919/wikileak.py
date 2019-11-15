import requests, bs4

url = "https://file.wikileaks.org/file/"
wiki = requests.get(url)
bswiki = bs4.BeautifulSoup(wiki.text, 'html.parser')

atag = bswiki.find_all('a')
href_list = []
for href in atag:
    href_list.append(href.get('href'))

pdf_list = []
for link in href_list:
    if '.pdf' in link:
        pdf_list.append(link)

header_list = [
    #遨游
    {"user-agent" : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
    #火狐
    {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
    #谷歌
    {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
]

import random
header = random.choice(header_list)

def download_file(pdf_name):
    response = requests.get("https://file.wikileaks.org/file/" + pdf_name,headers=header)
    with open(pdf_name, 'wb') as file:
        file.write(response.content)


i = 0
for pdf in pdf_list:
    download_file(pdf)
    i += 1
    print(i)
