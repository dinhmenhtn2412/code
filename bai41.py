f=open("list.txt","r")
i=0
for line in f:
	i+=1
	print(line, end="")
f.close()
print("\nTong so dong la: ",i)