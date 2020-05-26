import numpy as np 
x=np.random.randint(0,10) #random ra phần tử bất kỳ
x=[]
y=[]
for i in range(10):
	x.append(np.random.randint(1,10))
	y.append(np.random.randint(1,10))
print(x,y)
x=np.array(x)
y=np.array(y)
np.add(x,y)
np.maxium(x,y)
np.minium(x,y)
np.sqrt(x)
np.square(x,y)