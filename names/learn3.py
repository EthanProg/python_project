from pandas import Series, DataFrame
import pandas as pd
import numpy as np
# rng = pd.date_range('1/1/2013',periods=100,freq='D')
# # print(rng)
# data = np.random.randn(5, 4)
# print(data)
# cols = pd.MultiIndex.from_tuples([ (x,y) for x in ['A','B','C'] for y in ['O','I']])
# print(cols)

# print(range(3))
#
# df1 = DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
# df2 = DataFrame({'key':['a','b','d'],'data2':range(3)})
#
# print(df1)
# kk = 12312L
# print(str(kk))
# print(repr(kk))
# tt = [1,2,3,4,5]
# ss = [1,2,9]
# qq = []
# for a in ss:
#     qq.append(a in tt)
# print(qq)

# website = 'http://www.eee.org'
# website = list(website)
# website[-3:] = 'com'
# aa = ''
# for a in website:
#     aa += a
# print(aa)

# print('age',3)
# print(1<9<100)

# print(1 <9 and 9< 100)
# a = 2
# assert  a<10 and a >3
# aa = range(9,0,-1)
# print(aa)

# print([x*x for x in range(0,9,2)])
# aa = [x*x for x in range(9,0,-2)]
# print(aa)
# print(type(aa))
# aa.reverse()
# print(aa)

# print([x*x for x in range(10) if x % 3 == 0])
#
# print([(x,y) for x in range(3) for y in range(3)])

# a = DataFrame([1,3,5,7,9])
#
# # print(a)
#
# print(a.quantile([.2,.5,.8]))

# print(help(DataFrame))


# 定义参数，*为元组，**为字典
# def func1(*pa,**pp):
#     print(pa)
#     print(pp)
#
# func1(1,2,3,1,a=6,c=8)

# print(5//2)

# print(map(str,range(10)))

# class Cc():
#     _k_ = 1
#     def _fun1(self):
#         print(self._k_)
#     def out(self):
#         print(self._k_)
#
# a = Cc()
# print(a._k_)
# print(a.out(a))