class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def info(self):
		print("Chao ban toi ten la: ",self.name,"Tuoi cua toi la:",self.age)

class Student(Person):
	def __init__(self,name,age,grade):
		Person.__init__(self,name,age)
		self.grade=grade
	def infoGrade(self):
		print("Toi hoc lop:",self.grade)
hsa=Student("Duong Dinh","19","12/12")
hsa.info()
hsa.infoGrade()