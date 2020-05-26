import numpy as np
x=np.random.randint(1,10)
x=[]
y=[]
for i in range(10):
	x.append(np.random.randint(1,10))
	y.append(np.random.randint(1,10))
	
x.sort()
np.unique(x)
np.greater(x,y) #so sánh các phần tử tương ứng của x, y với x>y;
b=np.greater(x,y)
 b.all()# tất cả p tử đều đúng, nếu sai >>> false
 b.any()# bất kì p tử đúng  nếu có >>> true
np.equal(x,y) #xem các phần tử tương ứng có bằng nhau không
