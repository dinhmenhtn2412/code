try:
	a=100
	b=0
	x=a/b
	print("x= ",x)
	f=open("teoaa.txt","r")
	for line in f:
		print(line)
except ZeroDivisionError as error:
	 print("loi: ",error)
except FileNotFoundError as error:
	 print("loi: ",error)
