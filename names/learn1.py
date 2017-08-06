import pandas as pd
import matplotlib.pyplot as plt
# 读取数据
names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
# print(names1880)
names1880['year'] = '1880'
# print(names1880);
print(names1880.index)
# print(names1880.T)
# print(names1880)
# print(names1880.sort_values(by='births',ascending=False).head())
