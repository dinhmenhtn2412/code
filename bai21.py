print("----BAI 21-----")
a=[1,2,3,4,5,6]
b=[]
for i in a:
	b.append(i**2)
print(b)
#cách viêt gọn:
c=[i**2 for i in a if i%2==0]
print(c)
d=[(i,j) for i in a for j in c]
print(d)
print("done")
