class People(object):
    def __init__(self, name):
        print("Ten la: {:-^15}".format(name))
class Student(People):
    def __init__(self,name,age):
        People.__init__(self,name)
        print("Tuoi: ",age)
dinh=Student("Dinh",20)
