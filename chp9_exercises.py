# def test():
	# print("blah")
	
# def bruh():
	# duh = print(input("What is your name?"))
	# try:
		# if duh == "":
			# print("it works")
	# except:
		# print("nope")


#classes

#declared a class caled dog, classes should be uppercase
# class Dog:
	
	# def __init__(self, name, dogType, age):
		
		# self.name = name
		# self.dogType = dogType
		# self.age = age
		
#object example 1
# dog_01 = Dog('spot', 'akita', 3)
# print(f'My dog\'s name is {dog_01.name.title()}.')
# print(f'My dog is a type {dog_01.dogType.title()}.')
# print(f'My dog is {dog_01.age} years old.')
# print()


class Dog:
	
	def __init__(self, name, dogType, age):
		
		self.name = name
		self.dogType = dogType
		self.age = age
		
	def rollover(self):
		print(f'{self.name.title()} has rolled over.')
		if self.age < 2:
			print(f'very good for a {self.dogType.title()} that is {self.age} year old.')
		else:
			print(f'very good for a {self.dogType.title()} that is {self.age} years old.')
		
	def sit(self):
		print(f'{self.name.title()} is now sitting.')


dog_01 = Dog('speedy', 'greyhound', 2)
dog_01.rollover()
dog_01.sit()
# print(f'My dog\'s name is {dog_01.name.title()}.')
# print(f'My dog is a type {dog_01.dogType.title()}.')
# print(f'My dog is {dog_01.age} years old.')
print()

dog_02 = Dog('frisky', 'beagle', 1)
dog_02.rollover()
dog_02.sit()
# print(f'My dog\'s name is {dog_01.name.title()}.')
# print(f'My dog is a type {dog_01.dogType.title()}.')
# print(f'My dog is {dog_01.age} years old.')
print()
