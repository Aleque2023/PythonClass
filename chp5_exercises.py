# cars = ['audi','bmw','subaru','toyota']

# for car in cars:
	# if car == 'bmw':
		# print(car.upper())
	# else:
		# print(car.title())



# car = 'bmw'
# print(car == 'bmw')



# gym = 'plate'
# print("Is gym == 'plate'? I predict True.")
# print(gym == 'plate')

# print("\nIs gym == 'cashier'? I predict False.")
# print(gym == 'cashier')



# alien_color = 'red'
# if alien_color == 'green':
	# print("You earned 5 points!")
# if alien_color == 'red':
	# print("You earned 5 points for red!")

# alien_color2 = 'yellow'
# if alien_color2 != 'green':
	# print("\nYou just earned 10 points!")
# elif alien_color2 == 'green':
	# print("\n You earned 5 points for shooting a green alien.")



# alien_color3 = 'red'
# if alien_color3 == 'green':
	# print("You earned 5 points.")
# elif alien_color3 == 'yellow':
	# print("You earned 10 points.")
# else:
	# print("You earned 15 points.")



# age = int(input("Please enter your age: "))
# if age < 2:
	# print("You are still a baby")
# elif age >= 2 and age < 4:
	# print("You are a toddler")
# elif age >= 4 and age < 13:
	# print("You are a kid")
# elif age >= 13 and age < 20:
	# print("You are a teenager")
# elif age >= 20 and age < 65:
	# print("You are an adult")
# else:
	# print("You are an elder")

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
	# if requested_topping in available_toppings:
		# print(f"Adding {requested_topping}.")
	# else:
		# print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making your pizza!")


# names = ['tom', 'sauron', 'admin', 'mort', 'julian']
# for name in names:
	# if name == "admin":
		# print(f"Hello {name}, would you like to see a status report?")
	# else:
		# print(f"Hello {name}, thank you for logging in again.")

# usernames = []

# if usernames:
	# if username == "admin":
		# print(f"Hello {username}, would you like to see a status report?")
# else:
	# print("\nWe need to find some users!")


show = 'breaking bad'

if show == 'breaking bad':
	print("That's my favorite show!")
elif show == 'game of thrones':
	print("When is winds of winter coming out?")
else:
	print("What else should I binge?")

games = input("What game should I play? ")

match games:
	case "Hades":
		print("I already beat it!")
		
	case "Sekiro":
		print("I'm almost done with it.")
