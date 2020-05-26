def ham (start,length,step):
    i=start
    while i < length:
        yield i
        i+=step
d=list(ham(0,5,1))
print(d)