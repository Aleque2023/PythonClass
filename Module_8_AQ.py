###Alex Quezada, 9/6/2023, Module 8 Assignment
###Using function to convert miles to kilometers

kilo = 1.609

def milekilo(mi):
	try:
		mi = float(mi)                                                                                       #It tries to convert mi to float, if it fails it goes to the except block. In other words, it tests the user input.
		if mi < 0:
			print("\nDo not include a negative number.\n\nPlease run this program again.")                   #If a negative number is entered, that message will be printed out
		else:
			converted = round(float(mi * kilo), 3)
			print(f"\nYou have driven {mi} miles and {converted} kilometers!")
	except:
		print(f"\nThat is not a number.\n\nPlease run this program again.")

milekilo(input(f"How many miles have you driven? "))
