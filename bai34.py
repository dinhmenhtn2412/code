def Myrage(*Data):
    if(len(Data)==3):
        start=Data[0]
        step=Data[1]
        end=Data[2]
    elif(len(Data)==2):
        start=Data[0]
        step=1
        end=Data[1]
    else:
        start=0
        step=1
        end=Data[0]
    i=start
    while i<end:
        yield i
        i+=step
a=list(Myrage(0,3,10))
print(a)
print("-"*10)
			