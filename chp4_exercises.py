# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
	# print(magician)
	# print(f"{magician.title()}, that was a great trick!")
	# print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

#--------------------------------------

# Pizzas = ["Beef", "Pepperoni", "Cheese"]
# for Pizza in Pizzas:
	# print("I like " +Pizza+ " pizza.")
# print("I really love pizza!")

#--------------------------------------

# Animals = ["Dog","Cat","Rat"]
# for Animal in Animals:
	# print("A " +Animal+ " would make a great pet.")
# print("Any of these animals would make a great pet!")

#--------------------------------------

# for value in range(1,6):
	# print(value)

# numbers = list(range(1,6))
# print(numbers) #This will print out the list

# even_numbers = list(range(2, 11, 2))
# print(even_numbers) #The 2nd 2 in the range I think means how much it'll add

# squares = []
# for value in range(1, 11):
	# square = value ** 2
	# squares.append(square)
# print(squares)

# Shorter way to do that is

# squares = []
# for value in range(1, 11):
	# squares.append(value**2)
# print(squares)

# An even faster way is that, and is called list comprehension

# squares = [value**2 for value in range(1, 11)]
# print(squares)


# digits = [1,2,3,4,5,6,7,8,9,0]
# print(digits)
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# values = []
# for value in range (1, 21):
	# values.append(value)
# print(values)

# values = []
# for value in range (1,1000001):
	# values.append(value)
# print(values)
# print(min(values))
# print(max(values))
# print(sum(values))

# values = []
# for value in range (1, 20, 2):
	# values.append(value)
# print(values)

# threes = []
# for value in range (3, 31, 3):
	# threes.append(value)
# print(threes)

# cubed = []
# for value in range(1,11):
	# cubed.append(value**3)
# print(cubed)

# final = [value**3 for value in range (1,11)]
# print(final)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# magicians = ['alice', 'david', 'carolina', 'tom', 'jerry']
# for magician in magicians:
	# print(magician)
# print('The first three items in the list are: ' + str(magicians[:3]))
# print('Three items from the middle of the list are: ' + str(magicians[1:4]))
# print('The last three items in the list are: ' + str(magicians[2:]))

# Pizzas = ["Beef", "Pepperoni", "Cheese"]
# friend_pizza = Pizzas[:]
# Pizzas.append("Hawaiian")
# Pizzas.sort()
# friend_pizza.append("Bacon")
# friend_pizza.sort()
# print("My favorite pizzas are: ")
# for Pizza in Pizzas:
	# print(Pizza)
# print("\nMy friend's favorite pizzas are: ")
# for pizza in friend_pizza:
	# print(pizza)

# foods = ("egg", "bacon", "chicken", "pork", "goat")
# for food in foods:
    # print(food)
# foods = ("\negg", "rice", "chicken", "beans", "goat")
# for food in foods:
	# print(food)

# test = [1,2,3,4,5]
# tuppletest = (1,3,5,7)
# test2 = test[:]
# test2.append(9)
# tuppletest.append(8)
# test.append(8)
# print(test2)
# print(test)

# Original = ["Tarzan", "Peter", "Tom", "Frodo", "Brian"]

# Copy1 = Original[:] 
# #The colon means that it is taking the first element all the way to the last element of the list in the variable Original to the variable Copy1.

# Copy1.append("Walter")
# Original.append("White")
# #To prove that they are separate lists, I appended another unique element to each list.

# print(f"This is the copy of the original. {Copy1}")
# print(f"This is the original list. {Original}")

Original = ("Tarzan", "Peter", "Tom", "Frodo", "Brian")

Copy1 = Original[1:] 
#The colon means that it is taking the first element all the way to the last element of the list in the variable Original to the variable Copy1.

print(f"This is the copy of the original. {Copy1}")
print(f"This is the original list. {Original}")
print(len(Original))
print(len(Copy1))
