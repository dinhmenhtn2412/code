import pandas as pd
import numpy as np
from pandas import Series , DataFrame
from numpy.random import randn
s1=Series([10,14,12,15,19])
s2=Series([10,14,12,15,19],index=['A','B','C','D'])
diem=[5,6,7,8]
hs=["Teo","Ty","Tuan","Tun"]
s3=Series(diem, index=hs)

s3['Tuan'] #kết quả trả về sẽ là 7
