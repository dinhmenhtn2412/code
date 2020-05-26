f1=open("write.txt","w")
f=open("list.txt","r")
for line in f:
	print(line, file = f1, end="")
f.close()
f1.close()
print("done")
