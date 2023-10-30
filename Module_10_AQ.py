###Alex Quezada, 10/1/2023, Module 10 Assignment
###File Processing Activities

import os

path = input("What directory would you like to save your file in: ")

try:
	if os.path.isdir(path): #If the directory does not exist, it will print the string in the except
		name = input("What would you like to name this file: ")
		combined = path + name + ".txt"
		named = combined
		print(named)
		
	with open(named, "w") as file_object:
		file_object.write(f"{input('What is your name: ')}, ")
		file_object.write(f"{input('What is your address: ')}, ")
		file_object.write(f"{input('What is your phone number: ')} ")
		file_object.close()
		
	with open(named, "r") as file_object:
		for line in file_object:
			print(line)
		file_object.close()
except:
	print("Directory does not exist")
