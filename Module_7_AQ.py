###Alex Quezada, 9/4/2023, Module 7 Assignment
###Investment using while loop

print(f"Welcome to my while loop program!\n")
starting = float(input(f"What is the initial investment amount? "))
interestrate = float(input(f"What is the interest rate? "))
ending = starting * 2    #The variable ending is double the starting amount
years = 0

while starting < ending: #It will keep on running until the variable starting exceeds the variable ending
	years += 1
	starting = starting + round((starting * interestrate),2)
print(f"It has taken {years} years to double your investment!")
print(f"Your investment's current amount is ${round(starting, 2)}.")
