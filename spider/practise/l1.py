# coding: UTF-8
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("device_status_info.html"), "lxml")

print(soup.title)