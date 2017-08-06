import pandas as pd
# data = [[1,2,3],[4,5,6]]
# index = [0,1]
# columns = ['a','b','c']
# df = pd.DataFrame(data=data,index=index,columns=columns)
# print(df)
# print(df.loc[0])

# import pandas as pd
# data = [[1,2,3],[4,5,6]]
# index = ['d','e']
# columns=['a','b','c']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# print (df.iloc[1])

import pandas as pd
import numpy as np
df = pd.DataFrame({'key1':['a','a','b','b','a'],
                'key2':['one','two','one','two','one'],
                'data1':np.random.randn(5),
                'data2':np.random.randn(5)})
print(df)
grouped = df.groupby(df['key1'])
print(grouped.mean())
