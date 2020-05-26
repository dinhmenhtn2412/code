import pandas as pd
import numpy as np
from pandas import Series, Dataframe
from numpy.random import randn
df1=pd.read_clipboard()
df1.drop('D') #k lấy hàng D
df1.drop('Col2', axis=1)# k lấy cột

df2=DataFrame(np.arange(4).reshape(2,2), columns= list('AB'), index=list('XY'))
#tạo DataFrane
df3=DataFrame(np.arange(9).reshape(3,3), columns= list('ABC'), index=list('XYZ'))
df2+df3 #cộng Data frame
df2.add(df3,fill_value=0) # cộng hai DataFrame
