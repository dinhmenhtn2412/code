"""import array as arr
a = arr.array('i',[2, 4, 6, 8])
i=0
while i<4:
	print(a[i])
	i+=1
	pass
#print(a[0:4])
a[0:4]=arr.array('i',[1,3,5,7])
a.remove(1)
print(a.pop(2))
"""
import array as arr
import numpy as np
a=np.arange(0,10,2)
print(type(a))
print(a.shape)
b=[1,2,3,4,5]
b=arr.array("i",b)
for i in b:
    if(i>2):
        print(i, end=" ")
c=arr.array("i")
c=a+b
print(c)