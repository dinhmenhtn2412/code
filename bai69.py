import pandas as pd
import numpy as np
from pandas import Series, Dataframe
from numpy.random import randn
diem=[5,6,7,8]
hs=["Ty","Teo","Tuan","Tun"]
s3=Series(diem,index=hs)
df1=pd.read_clipbroad()
df1.columns #lấy ra tên các cột
df1.head() # lấy ra 5 hàng đầu tiên
df1.tail()# lấy ra 5 hàng cuối
df1.name # lấy ra cột name
df1.name='Duong Dinh' đổi toàn bộ các tên trong cột
