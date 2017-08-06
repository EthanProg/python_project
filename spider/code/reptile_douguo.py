import socket
import urllib
from urllib import request
from urllib.error import HTTPError

import time
from urllib.parse import quote, unquote
from urllib.request import urlopen


import re

from bs4 import BeautifulSoup

# 设置超时的时间为10s
from spider.pub.pub import DealDataInDb

_timeout = 10
# 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
socket.setdefaulttimeout(_timeout)
# 休眠暂停
_sleep_download_time = 10
# 爬的食品数量
GLOBAL_1 = 0


# 取菜系分类地址
def reptile_sort_url():
    try:
        main_url = "http://www.douguo.com/caipu/fenlei"
        req = request.Request(main_url)
        # 加入请求头
        user_agent_1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        user_agent_2 = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"
        req.add_header("User-Agent", user_agent_1 + user_agent_2)
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
        req.add_header("Cache-Control", "max-age=0")

        main_text = urlopen(req, None, timeout=_timeout)
        main_obj = BeautifulSoup(main_text, "html.parser")
        for every_sort_url in main_obj.find(id="ddd2").findAll("a", href=re.compile("http://www.douguo.com/caipu/")):
            if 'href' in every_sort_url.attrs:
                reptile_page_url(every_sort_url.attrs['href'], every_sort_url.get_text())
                # print(every_sort_url.get_text() + "---" + every_sort_url.attrs['href'])

    except HTTPError as e:
        print("HTTPError", e)
    except UnicodeDecodeError as e:
        time.sleep(_sleep_download_time)
        print("UnicodeDecodeError", e)
    except urllib.error.URLError as e:
        time.sleep(_sleep_download_time)
        print("URLError", e)
    except socket.timeout as e:
        time.sleep(_sleep_download_time)
        print("timeout", e)


# 取每个菜系每个分页url
def reptile_page_url(every_sort_url, every_sort_name):
    try:
        # print(every_sort_url)
        every_sort_url = every_sort_url.replace("http://", "")
        every_sort_url = "http://" + quote(every_sort_url)
        # print(every_sort_url)
        req = request.Request(every_sort_url)
        # 加入请求头
        user_agent_1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        user_agent_2 = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"
        req.add_header("User-Agent", user_agent_1 + user_agent_2)
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
        req.add_header("Cache-Control", "max-age=0")

        every_sort_text = urlopen(req, None, timeout=_timeout)
        every_sort_obj = BeautifulSoup(every_sort_text, "html.parser")

        last_url = every_sort_obj.findAll(style="cursor: pointer;")[-1].a.attrs['href']
        every_sort_url = unquote(every_sort_url + '/')
        pag_num = last_url.replace(every_sort_url, "")
        pag_num = int(pag_num) / 30
        for i in range(0, int(pag_num)):
            page_index = i * 30
            every_page_url = every_sort_url + str(page_index)
            every_detail(every_page_url, every_sort_name)

    except HTTPError as e:
        print("HTTPError", e)
    except UnicodeDecodeError as e:
        time.sleep(_sleep_download_time)
        print("UnicodeDecodeError", e)
    except urllib.error.URLError as e:
        time.sleep(_sleep_download_time)
        print("URLError", e)
    except socket.timeout as e:
        time.sleep(_sleep_download_time)
        print("timeout", e)
    except TypeError as e:
        print("TypeError", e)


# 取每页美食的详细信息
def every_detail(every_detail_url, every_sort_name):
    try:
        every_detail_url = every_detail_url.replace("http://", "")
        every_detail_url = "http://" + quote(every_detail_url)

        req = request.Request(every_detail_url)
        # 加入请求头
        user_agent_1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        user_agent_2 = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"
        req.add_header("User-Agent", user_agent_1 + user_agent_2)
        req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
        req.add_header("Cache-Control", "max-age=0")

        detail_text = urlopen(req, None, timeout=_timeout)
        detail_obj = BeautifulSoup(detail_text, "html.parser")
        for every_detail_html in detail_obj.find(id="container").findAll(class_="cp_box"):
            browse_info = every_detail_html.p.get_text()  # 浏览量 收藏量 已学做
            food_url = every_detail_html.a.attrs['href']  # 美食链接
            food_name = every_detail_html.img.attrs['alt']  # 美食名称
            every_detail_url = unquote(every_detail_url)
            # print(every_detail_url + "---" + browse_info + "---" + food_name + "---" + food_url + "---" + every_sort_name)
            add_mysql_food_info(every_detail_url, browse_info, food_name, food_url, every_sort_name)


    except HTTPError as e:
        print("HTTPError", e)
    except UnicodeDecodeError as e:
        time.sleep(_sleep_download_time)
        print("UnicodeDecodeError", e)
    except urllib.error.URLError as e:
        time.sleep(_sleep_download_time)
        print("URLError", e)
    except socket.timeout as e:
        time.sleep(_sleep_download_time)
        print("timeout", e)
    except TypeError as e:
        print("TypeError", e)


# 处理数据
def add_mysql_food_info(every_detail_url, browse_info, food_name, food_url, every_sort_name):
    now_date = time.strftime('%Y%m%d%H%M%S', time.localtime())
    goods_list_line = []  # 每行食品信息
    browse_info_list = browse_info.split("·")
    browse_num = ""
    collection_num = ""
    finished_num = ""
    if len(browse_info_list) == 3:
        browse_num = str(browse_info_list[0]).replace("浏览", "")
        collection_num = str(browse_info_list[1]).replace("收藏", "")
        finished_num = str(browse_info_list[2]).replace("已学做", "")
    goods_list_line.append(food_name.replace(" ", ""))
    goods_list_line.append(food_url.replace(" ", ""))

    goods_list_line.append(browse_num.replace(" ", ""))
    goods_list_line.append(collection_num.replace(" ", ""))
    goods_list_line.append(finished_num.replace(" ", ""))
    goods_list_line.append(every_detail_url.replace(" ", ""))
    goods_list_line.append(every_sort_name.replace(" ", ""))
    goods_list_line.append(" ")
    goods_list_line.append(now_date)
    tuple_foods = tuple(goods_list_line)
    global GLOBAL_1
    GLOBAL_1 = int(GLOBAL_1) + 1
    print(str(GLOBAL_1) + "---" + str(tuple_foods))

    # 写入文件
    #file_Write("豆果美食.txt", str(tuple_foods)+"\n")

    # 写入数据库
    sql = 'INSERT INTO DOUGUO (FOODS_NAME, FOODS_DETAIL_URL, BROWSE_NUM, COLLECTION_NUM, FINISHED_NUM, FOODS_URL, FOODS_SORT, NOTE, CREATE_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    dealdb = DealDataInDb()
    dealdb.sql_insert(sql, tuple_foods)


def main():
    reptile_sort_url()


if __name__ == '__main__':
    main()
