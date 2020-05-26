def tong(n1,n2,n3,*data,**list):
	t1=t2=t3=0
	t1=n1+n2+n3
	for i in data:
		t2+=i
	for k,j in list.items():
		t3+=j
	t=[t1,t2,t3]
	return(t)
t=tong(10,20,30,11,12,13,14,15,a=100,b=200,c=300)
print(t)
print('done')