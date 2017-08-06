from pandas import Series,DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import randn
# obj = Series([4,5,6,7])
# print(obj)
# print(obj.values)
# print(obj.index)
# df = pd.read_csv('ca_gray_users.txt')
# print(df)
# df = pd.read_table('ca_gray_users.txt',names=['ORG_CODE','TENANT_ID','GRAY_SCALE'])
# print(df)
# fig = plt.figure()
# print(fig)
# ax1 = fig.add_subplot(2,2,1)
plt.plot(randn(50).cumsum(),'k--')