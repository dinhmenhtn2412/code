import pandas as pd
import numpy as np
from pandas import Series, Dataframe
from numpy.random import randn
sinhvien=['Teo','Ty','Tun','Tuan','Tien']
data={'diem' : diem, 'sinhvien' : sinhvien}
df2=Dataframe(data) #chuyển diction thành dataframe

indx='A B C D E'.split()
cols='Col1 Col2 Col3 Col4 Col5'.split()
x=[]
for i in range(25):
    x.append(np.random.randint(1,100))
x= np.array(x)
x=x.reshape(5,5)

df3=DataFrame(x,index=indx,columns=cols)
#reindex row
newind='A B C D E F G'.split()
df4=df3.reindex(newind, fill_value=0)
#reindex columns
cols='Col1 Col2 Col3 Col4 Col5 col6 col7'.split()
df4=df3.reindex(columns=cols, fill_value=0)
df4