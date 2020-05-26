import pandas as pd
import numpy as np
from pandas import Series , DataFrame
from numpy.random import randn
diem=[5,6,7,8]
hs=["Ty","Teo","Tuan","Tun"]
s3=Series(diem,index=hs)
s3a=s3.to_dict() #chuyển sang kiểu dict
s3a
 #out put: {'Ty': 5, 'Teo': 6, 'Tuan': 7, 'Tun': 8}
4b=Series(s3a) #lại chuyển về như cũ
pd.isnull(s4) # kiểm tra các giá trị là trống
pd.notnull(s4)# kiểm tra giá trị là sai.
s3+s4 # cộng hai giá trị tương ứng của mỗi phần tử.
s.name="Danh Sach"
