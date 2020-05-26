std={'hs1':'Duong','hs2':'van','hs3':'dinh'}
del std['hs1']
print(std.keys())
c=std.values() 
print(c)

print(std)
i=std.items()
for item in i:
	print(item[1], end=" ")