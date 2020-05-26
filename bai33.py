def countchar (*data):
	dic={}
	for item in data:
		for i in item:
			i=i.upper()
			if i in dic:
				dic[i]=dic[i]+1
			else:
				dic[i]=1
	return dic
a=countchar("Duong","Van", "Dinh")
print(a)
print('----------done---------')

def CountChar(*Data):
    Dict={}
    for item in Data:
        for i in item:
            i=i.lower()
            if i in Dict:
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
    return Dict
b=CountChar("Tinh yeu anh trao em nhu song bien chieu HHHom")
print(b)
print("{:-^11}".format("DONE"))
