import requests

# res = requests.get("https://www.jd.com")

res = requests.get("https://dig.chouti.com",headers={
    "User-Agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
})
# 响应体
with open("demo.html","w",encoding="utf8") as f:
    f.write(res.text)