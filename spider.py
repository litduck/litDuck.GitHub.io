import urllib.request
import urllib.error

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取数据
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250"
    # 3.保存数据
    #saveData(savepath)

    askURL("https://movie.douban.com/top250?start=")

# 爬取数据
def getData(baseurl):
    datalist = []
    for i in range(0,10):       # 调用获取页面信息的函数·10次
        url = baseurl + str(i*25)
        html = askURL(url)      # 保存获取到的页面源码

        # 2.逐一解析数据


    return datalist

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
    return html


# 3.保存数据
def saveData():
    print('save....')

if __name__ == '__main__':
    main()
