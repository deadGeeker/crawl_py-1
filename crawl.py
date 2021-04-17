import requests as rs
import re
import time

# 指定目标网站
urls = "https://app.mi.com/topList?"
# 根据自己浏览器中的User-Agent进行赋值
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}



# 将数据存储到本地
def img_save(img_url, name):
    img_req = rs.get(url=img_url, headers=headers)
    if img_req.status_code == rs.codes.ok:
        data = img_req.content
        with open("{}.png".format(name), "wb") as f:
            f.write(data)
            print("{} - 图片存储完毕".format(name))

# 爬取数据
def crawl_f(page):
    url = urls + "page={}".format(page)
    # print(url)
    print("第{}页".format(page))
    req = rs.get(url=url, headers=headers)
    if req.status_code == rs.codes.ok:
        html = req.text
        pattern = re.compile(
            r'<li><a href="/details(.*?)"><img data-src="(.*?)" src="(.*?)" alt="(.*?)" width="(.*?)" height="(.*?)"></a><h5><a href="(.*?)">(.*?)</a></h5><p class="(.*?)"><a href="(.*?)">(.*?)</a></p></li>')
        # m为一个列表，长度为48，列表中的每一个元素包含对应应用的相关信息
        m = pattern.findall(html)
        # n为元组，长度为11, n1为应用图片链接, n3为应用名字, n10为应用类别
        for n in m:
            # 开始存储图片
            img_save(n[1], n[3])

# 爬取42页数据，爬取间隔为3秒
for i in range(1, 43):
    crawl_f(i)
    time.sleep(3)
