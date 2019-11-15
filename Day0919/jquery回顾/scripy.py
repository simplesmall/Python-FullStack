import random
import requests
from PIL import Image
from io import BytesIO

header_list = [
    #遨游
    {"user-agent" : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
    #火狐
    {"user-agent" : "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
    #谷歌
    {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
]

# proxy_list = [
#     {"http" : "112.115.57.20:3128"}
#     # {"http" : "root:01@124.88.67.81:80"}
# ]

header = random.choice(header_list)


for i in range(1,269):
    img_src = 'https://babel.hathitrust.org/cgi/imgsrv/image?id=uc1.31822006410914;seq='+str(i)+';size=100;rotation=0'
    response = requests.get(img_src,headers = header)
    image = Image.open(BytesIO(response.content))
    image.save('F:/BeautifulPictures/book/'+str(i)+'.jpg')

print("Finished!!!")