import pandas as pd
import numpy as np
from pandas import Series , DataFrame
from numpy.random import randn
s2=Series([10,12,14,15], index=["A","B","C","D"])
diem=[5,6,7,8]
hs=["Ty","Teo","Tuan","Tun"]
s3=Series(diem,index=hs)


s4=Series([1,3,4,5,6], index=['A','B','C','D','E'])
s5=Series([7,8,9], index=['A','B','C'])

s4+s5  #cộng các phần tử tương ứng
		#nếu ko có gia trị tư ở 1 trong 2 trả vể NaN (rỗng)
ind="a b c d e f g h".split() #8 p tử tạo thảnh index, tác
