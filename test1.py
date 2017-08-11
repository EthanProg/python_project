# 引入模块
# -*- coding:utf-8 -*-

# 常用包的函数
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# 解决显示汉字不正确问题
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False



# dd = '210202128620.00'
#
# print(dd[:-3])

# aa = [1,2,3]
# print(aa.index(1))

# print(range._doc_)

# from TKinter import *

# aa = [1,2,3]
# bb = DataFrame(aa,columns=['a','b','c'])
# print(bb)

# data = [5, 20, 15, 25, 10]
#
# print(range(len(data)))
#
# plt.bar(range(len(data)), data, color='rgb') # or `color=['r', 'g', 'b']`
# plt.show()
# ss = 'asdasd'
# print(ss.isalnum())

# print(0 if 1>3 else 5)

import sqlite3

a = '201705011'

print(a[0:8])
