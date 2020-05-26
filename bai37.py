class student(object):
	def __init__(self,name,age):
		print("Name:",name, "  Age:",age)
	def __str__(self):
		return("--------------")
teo=student("Tony teo","19")
print(teo)
