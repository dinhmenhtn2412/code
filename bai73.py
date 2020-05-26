import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from numpy.random import randn
df1=pd.read_clipboard()#đọc bảng từ clipboard
df1.sum() #tính tổng các cột
df1.sum(axis=1)#tính tổng các hàng
df1.max()# trả về giá trị lớn nhất của mỗi cột
df1.idxmax()# trả về idx của giá trị max ở mỗi cột
df1.cumsum()# tính tổng dần từ trên xuống:
			# hàng 2=h1=h2;h3=h1+h2+h3
df1.describe()# mô tả bảng

nd=np.nan # hàm nào đó
A=[1,2,3]
B=[4,nd,6]
C=[nd,8,nd]
D=[nd,nd,nd]
df2=DataFrame([A,B,C,D])
df2.dropna() # drop hàng nào có ô giá trị NaN
df2.dropna(how='all') # drop hàng tất cả các ô đều NaN
df2.dropna(thresh=1) # drop một dòng từ dưới lên
df2.fillna(100) # thay ô có giá trị NaN thành 100
df2.fillna(24,inplace = True) # thay ô có giá trị NaN thành 24
df2
