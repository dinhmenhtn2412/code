import pandas as pd
import numpy as np
from pandas import Series , DataFrame
from numpy.random import randn
s2=Series([10,12,14,15], index=["A","B","C","D"])
diem=[5,6,7,8]
hs=["Ty","Teo","Tuan","Tun"]
s3=Series(diem,index=hs)

#lấy key index
s3.index
s3.values #lấy values.
s3[2]#lấy phần tử thứ 2
s3[2:]# lấy từ phần tử thứ 2


x=list(range(11,16))
ind=['A','B','C','D','E']
s5=Series(x,ind)
ind2=['A','B','F']
s4=s5.reindex(ind2,fill_value=0) #Đổi index \