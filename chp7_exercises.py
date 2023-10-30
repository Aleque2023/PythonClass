# inactiveteams = ['cardinals', 'tigers', 'red sox', 'rangers', 'astros', 'white sox', 'cubs']
# activeteams = []
# currentteam = ''

# print('inactive teams')
# print(inactiveteams)
# print('active teams')
# print(activeteams)
# print()

# while inactiveteams:
	# currentteam = inactiveteams.pop(0)
	# print(f'The current team is {currentteam.title()}.')
	# activeteams.append(currentteam)

# print()
# print('inactive teams')
# print(inactiveteams)
# print('active teams')
# print(activeteams)
# print()

# people = input("How many people are attending? ")
# people = int(people)

# if people > 8:
	# print("You will need to wait for a table. ")
# else:
	# print("Your table is ready. ")


# prompt = "\nTell me something, and I'll repeat it: "
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
	# message = input(prompt)
	# print(message)



# prompt = "\nTell me something, and I'll repeat it: "
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# active = True
# while active:
	# message = input(prompt)
	
	# if message == 'quit':
		# active = False
	# else:
		# print(message)

# topping = []
# message = ''

# while message != 'quit':
	# message = input("What topping do you want?")
	# if message.lower() == 'quit':
		# print(f"You added {topping} to your pizza.")
		# break
	# print(f"I'll add {message} to your pizza.")
	# topping.append(message)
	
# infinite = 1
# while True:
	# infinite += 132534636253465346999999999999999999999999999999999999583497658924675290670765057029759023725096720560236570759120935716570913765
	# print(infinite)


# uncomfirmedusers = ['alice', 'brian', 'candace']
# confirmedusers = []

# while uncomfirmedusers:
	# currentusers = uncomfirmedusers.pop()
	
	# print(f"Verifying user: {currentusers.title()}")
	# confirmedusers.append(currentusers)

# print("\nThe following users have been confirmed:")
# for confirmeduser in confirmedusers:
	# print(f"\t\t\t\t\t",confirmeduser.title())


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
	# pets.remove('cat')

# print(pets)


responses = {}

polling_active = True

while polling_active:
	name = input("What is your name: ")
	response = input("Which mountain would you like to climb someday? ")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat.lower() == 'no':
		polling_active = False
		
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")
