import pandas as pd
import numpy as np
from pandas import Series , DataFrame
from numpy.random import randn
s2=Series([10,12,14,15], index=["A","B","C","D"])
diem=[5,6,7,8]
hs=["Ty","Teo","Tuan","Tun"]
s3=Series(diem,index=hs)

s3[1] # lấy phần tử thứ 1
s3[1]=30 # sửa phần tử thứ 1 thành 30
s4=s3*2 # nhân đôi giá trị tương ứng ở mảng s3
s3[['Ty', 'Tep']] # lấy ra mảng con gồm hai phần tử có index trên
s4[s4<10] # lấy ra phần tử nhỏ hơn 10
s4[s4==10] #lấy ra phần tử bằng 10