# BUFFERSIZE=1000000 #mỗi lần đọc 14000 byte, giá trị này có thể đổi
# rfile=open("data.txt","r")
# wfile=open('write.txt',"w") # mở file để đọc, ghi
# buffer=rfile.read(BUFFERSIZE)
# i=0
# while(len(buffer)>0):
# 	i+=1
# 	wfile.write(buffer)
# 	print(i,"{} byte".format(len(buffer)))
# 	buffer=rfile.read(BUFFERSIZE)
# rfile.close()
# wfile.close()
# print(" DONE")
# đã test và chạy rất hay hiha
lenr=2000000
fileR=open("data.txt","r")
fileW=open("test w.txt","w")
moilandoc=fileR.read(lenr)
i=0
while(len(moilandoc)>0):
	i+=1
	print("lan thu {:-^5} doc duoc {} bye".format(i,len(moilandoc)))
	moilandoc=fileR.read(lenr)
print("DONE!")
