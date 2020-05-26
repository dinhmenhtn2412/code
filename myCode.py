def geet(n):
	i=0
	while i<n :
		print("Duong Van Dinh")
		i+=1
def sumNume(*so):
	sum=0;
	for i in so:
		sum+=i
	return sum
def myrange(start,length, step):
	i=start
	while i < length:
		yield i
		i+=step