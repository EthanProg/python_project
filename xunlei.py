#!python3
import urllib.request

from lxml import etree
import threading
from multiprocessing.dummy import Pool as ThreadPool
from urllib.request import urlopen, Request
# 龙图腾原创

# 请求
# 三种浏览器的user-agent
from requests import request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}

# headers  = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

max_try_down = 20
max_timeout_down = 1
allresult = ""  # 最终要下载的内容
allresult_count = 1  # 下载个数

all_page_item = []

# 将下载结果总结到allresult
lock = threading.Lock()  # 线程锁初始化


def add_inresult(weburl, name, link, size):
    global allresult_count, allresult

    lock.acquire()  # 线程锁加锁
    if link not in allresult:
        allresult_count = allresult_count + 1
        allresult += ("%s\r\n" % (weburl))
        # allresult += ("len name=%d link=%d %d\r\n"%(len(name),len(link),len(size)))
        allresult += ("name=%s\r\n" % (name))
        allresult += ("size=%s\r\n" % (size))
        allresult += ("link=%s\r\n" % (link))
        allresult += ("\r\n")
    lock.release()  # 线程锁解锁


# 下载文件
def download_this(weburl):
    # print("down %s++\n"%(weburl),end='')#因为使用了threadpool故此打印\n可能会遇到问题，故此使用这种打印方法

    # 下载循环尝试4次
    for i in range(max_try_down):
        try:
            sub_req = urllib.request.Request(url=weburl, headers=headers)
            sub_response = urllib.request.urlopen(sub_req, timeout=max_timeout_down)
            sub_data = sub_response.read()
            sub_data = sub_data.decode('utf-8')
            tree = etree.HTML(sub_data)

            file_name = " ".join(tree.xpath(u"//h3/text()"))  # 找到h3的text
            file_size = tree.xpath(u"//b[text()='文件大小']/following-sibling::span")[
                0].text  # 找到文本="文件大小"的节点 following-sibling::span寻找下一个span节点
            file_link = tree.xpath(u"//a[@href=*]/@href")[0]  # 寻找存在href的 a节点，并且提取href
            add_inresult(weburl, file_name, file_link, file_size)
            break
        except IndexError as e:
            # add_inresult(weburl, file_name, "连接失效:" + weburl, file_size)
            # print(e)
            pass
        except Exception as e:
            # print("%s [download_this]重试 %d <%s>:%s\n" % (weburl, i, type(e), e), end='')
            # print(e)
            pass

    this_last_url = "https://www.soxunlei.com/"+(weburl)
    print(this_last_url)
    #print("down https://www.soxunlei.com/%s ok--\n" % (weburl), end='')  # 因为使用了threadpool故此打印\n可能会遇到问题，故此使用这种打印方法


# 列出当前页面的下载列表
def list_this(weburl):
    global all_page_item
    for i in range(max_try_down):
        try:
            # print("+++search+++%s\n"%weburl,end='');#因为使用了threadpool故此打印\n可能会遇到问题，故此使用这种打印方法
            request = urllib.request.Request(url=weburl, headers=headers)
            # 爬取结果
            response = urllib.request.urlopen(request, timeout=max_timeout_down)

            data = response.read()

            # 设置解码方式
            data = data.decode('utf-8')

            tree = etree.HTML(data)

            nodes = tree.xpath(u"//h5[@class='item-title']/a/@href")  # 找寻h5节点的class属性为item-title下的a节点/提取href属性

            if len(nodes) <= 0:
                return False

            all_page_item += nodes  # 统计所有的页面下的下载页面

            print("allresult_count=%d" % len(all_page_item))
            print("---search ok---%s \n" % weburl, end='')  # 因为使用了threadpool故此打印\n可能会遇到问题，故此使用这种打印方法
            return True
        except Exception as e:
            # print("%s [list_this]重试 %d <%s>:%s\n" % (weburl, i, type(e), e),end='')  # 因为使用了threadpool故此打印\n可能会遇到问题，故此使用这种打印方法
            # print(e)
            pass


def search_this(name):
    while True:
        try:
            url = "https://www.soxunlei.com/search/%s/page/%d.html" % (urllib.request.quote(name), 1)
            request = urllib.request.Request(url=url, headers=headers)
            # 爬取结果
            response = urllib.request.urlopen(request, timeout=1)

            data = response.read()

            # 设置解码方式
            data = data.decode('utf-8')

            tree = etree.HTML(data)

            count = int(tree.xpath(u"//ol[@class='breadcrumb']/li[4]/font[2]")[0].text)  # 搜索返回个数，并且算出有多少页
            page_count = count / 15 + 1  # 一页容纳15个下载页，算出页数
            print("%s搜索到%d个内容，分为%d页" % (name, count, page_count))

            # 讲下载页的url算出放入page_nodes
            page_nodes = []
            for n in range(1, int(page_count) + 1):
                url = "https://www.soxunlei.com/search/%s/page/%d.html" % (urllib.request.quote(name), n)
                page_nodes.append(url)
               # print("url=%s" % url)
            break
        except Exception as e:
            # print("%s:%s" % (type(e), e))
            pass
    # 调用python线程池模型，抓取所有下载页中的下载项
    pool = ThreadPool(32)
    results = pool.map(list_this, page_nodes)
    pool.close()
    pool.join()

    # 线程池模型,下载所有内容
    pool = ThreadPool(32)
    results = pool.map(download_this, all_page_item)
    pool.close()
    pool.join()

    print(allresult)
    print("抓取完成 项%d 下载%d" % (count, allresult_count))


if __name__ == "__main__":
    search_this("")
