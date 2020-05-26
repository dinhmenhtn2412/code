import pandas as pd
import numpy as np
from pandas import Series, Dataframe
from numpy.random import randn
df1=pd.read_clipboard()
df1['col1'] #chọn cột col1
df1[['col1','col2']] #cách chọn hai cột

df1[df1['Col3']>30] # lấy những hàng của Data lớn hơn 30 ở col3

df1>50 #trả về giá trị true false cho cả bảng
df1.ix['E'] # lấy hàng E hiện ko dùng đc nữa
df1.loc['E']
df1.iloc['E']

