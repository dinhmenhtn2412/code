f=open("data1.txt","r")
f.seek(10)
fpos=f.tell()
print("\n doc toi vi tri: ",fpos)

line=f.readline()
print(line, end="")
fpos=f.tell()
print(" \ndoc toi vi tri: ",fpos)

line=f.readline()
print(line, end="")
fpos=f.tell()
print(" \ndoc toi vi tri: ",fpos)

line=f.readline()
print(line, end="")
fpos=f.tell()
print(" \ndoc toi vi tri: ",fpos)


