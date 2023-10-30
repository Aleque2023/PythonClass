#Alejandro Quezada, 8/24/2023, Module 4 Assignment
#The purpose of this code is to create a tuple and follow the instructions

States = ('Montana', 'Wyoming', 'Utah', 'Texas', 'Ohio', 'Florida', 'Alabama', 'Iowa', 'Nebraska', 'Kansas', 'Maine', 'Delaware', 'Hawaii', 'Oregon', 'Nevada', 'Maryland', 'Alaska')
print(States) #I am printing the tuple that I just created

print()

for State in States:
    print(f"{State}") #Here I printed out each element in the tupple along with the f-string format

print()

for State in States[::-1]:
	print(f"{State}") #It prints in reverse, so it'll start with Alaska
