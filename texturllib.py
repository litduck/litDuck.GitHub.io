import urllib.request

# 获得一个get请求
# respond = urllib.request.urlopen("http://www.baidu.com")
# print(respond.read().decode('utf-8'))

# import urllib.parse
# data = bytes(urllib.parse.urlencode({'hello':'word'}),encoding='utf-8')
# respond = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(respond.read().decode('utf-8'))

# 超时处理
# try:
#     respond = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
# except urllib.error.URLError as e:
#     print("rime out!")


# respond = urllib.request.urlopen("http://www.baidu.com")
# #print(respond.status)
# print(respond.getheaders())
# print(respond.getheader('Set-Cookie'))

# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'hello':'word'}),encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# respond = urllib.request.urlopen(req)
# print(respond.read().decode('utf-8'))


# url = "http://www.douban.com"
# headers = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# req = urllib.request.Request(url=url, headers=headers)
# respond = urllib.request.urlopen(req)
# print(respond.read().decode('utf-8'))

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # #1、爬取数据
    # datalist = getData(baseurl)
    # savepath = ".\\豆瓣电影Top250"
    # #3、保存数据
    # #saveData(savepath)

    askURL(baseurl)

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        respond = urllib.request.urlopen(req)
        html = respond.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

main()
