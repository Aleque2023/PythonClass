# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# alientest = {}
# alientest['color'] = 'green'
# alientest['points'] = 5
# print(alientest)
# print(f"The alien is {alientest['color']}.")

# alientest['color'] = 'yellow'
# print(f"The alien is now {alientest['color']}.")


# alienspd = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': 5}
# print(f"Original position: {alienspd['x_position']}.")

# if alienspd['speed'] == 'slow':
	# x_increment = 1
# elif alienspd['speed'] == 'medium':
	# x_increment = 2
# else:
	# x_increment = 3

# alienspd['x_position'] = alienspd['x_position'] + x_increment
# print(f"New position: {alienspd['x_position']}.")

# del alienspd['points']
# print(alienspd)


# favorite_languages = {
    # 'jerry': 'python',
    # 'tom': 'java',
    # 'matt': 'python',
    # 'iroh': 'c#',
    # }
    
# language = favorite_languages['jerry'].title()
# print(f"Jerry's favorite language is {language}.")
# test = favorite_languages.get('points', "Doesn't exist.")
# print(test)


# firstworldseries = {
    # 'winningteam': 'red sox',
    # 'winningcity': 'boston',
    # 'year': 1903,
    # 'losingteam': 'pirates',
    # 'losingcity': 'pittsburgh',
    # }

# for key, value in firstworldseries.items():
	# print(f"Key: {key} Value: {value}")
	
# print()

# for key, value in firstworldseries.items():
	# if type(value) is int:
		# print(f"{key.title()} is {value}")
	# else:
		# print(f"{key.title()} is {value.upper()}")

#Looping through a dictionary in a particular order

# worldseries = {
    # 2017: 'astros',
    # 2007: 'red sox',
    # 2009: 'yankees',
    # 2015: 'royals',
    # 2006: 'cardinals',
    # 2011: 'cardinals',
    # 2018: 'red sox',
    # 2012: 'giants',
    # 2010: 'giants',
    # 2013: 'red sox',
    # 2008: 'phillies',
    # 2014: 'giants',
    # 2016: 'cubs',
    # 2019: 'nationals',
    # }

# print('-----------------------------------------------------------------')
# print('original')
# print('-----------------------------------------------------------------')

# for year in worldseries.keys():
	# print(f"The year played is {year}, the winning team was the {worldseries[year]}.")

# print('-----------------------------------------------------------------')
# print('-----------------------------------------------------------------')
# print('sorted')
# print('-----------------------------------------------------------------')

# for year in sorted(worldseries.keys()):
	# print(f"The year played is {year}, the winning team was the {worldseries[year]}.")

# print('-----------------------------------------------------------------')
# print('-----------------------------------------------------------------')
# print('sorted and uppercase')
# print('-----------------------------------------------------------------')

# for year in sorted(worldseries.keys()):
	# print(f"The year played is {year}, the winning team was the {worldseries[year].upper()}.")
	
	
	
	





# person = {
    # "first_name": "Jon",
    # "last_name": "Snow",
    # "age": 23,
    # "city": "The wall",
    # }
# for guy in person.values(): #using .items() will print out both the key and value together, using .keys() will just print the key, using .values() will just print the values.
	# print(guy)


# favnum = {
    # "Aegon": 20,
    # "Tyrion": 7,
    # "Bron": 2,
    # "Robb": 1,
    # "Ned": 0,
    # }
# favnum["Theon"] = 9
# for favorite in favnum.items():
	# print(favorite)


# words = {
    # "String": "A String is a data structure in Python that represents a sequence of characters",
    # "Integer": "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length",
    # "Float": "Float is a function or reusable code in the Python programming language that converts values into floating point numbers",
    # ".round()": "The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals",
    # ".strip()": "The strip() method removes any leading, and trailing whitespaces",
    # }
# for word in words.keys():
	# print(f"\nThe definition of {word} is: {words[word]}.")


# user_0 = {
    # 'username': 'efermi',
    # 'first': 'enrico',
    # 'last': 'fermi',
    # }

# for key, value in user_0.items(): #the key and value words in this line can be substitued with any word, it is arbitrary
	# print(f"\nKey: {key}")
	# print(f"\nValue: {value}")




# rivers = {
    # "nile": "egypt",
    # "ganges": "india",
    # "danube": "germany",
    # "seine": "paris",
    # }

# for a, b in sorted(rivers.items()):
	# print(f"\nThe {a.title()} runs through {b.title()}.")

# for key in rivers.keys():
	# print(f"\n{key.title()}")

# for value in rivers.values():
	# print(f"\n{value.title()}")





# favlang = {
    # 'tom': 'python',
    # 'jerry': 'c',
    # 'bob': 'ruby',
    # 'rick': 'java',
    # }

# name = ['rose','jerry','tom','walt','jesse']

# for duo in favlang.keys():
	# if duo in name:
		# print(f"\nThank you for taking the poll!")
	# else:
		# print(f"\nPlease take the poll {duo.title()}.")


# alien0 = {'color': 'green', 'points': 5}
# alien1 = {'color': 'yellow', 'points': 10}
# alien2 = {'color': 'red', 'points': 15}

# aliens = [alien0, alien1, alien2]

# for alien in aliens:
	# print(alien)


# aliens = []

# for alien_number in range(30):
	# new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	# aliens.append(new_alien)

# for alien in aliens[:3]:
	# if alien['color'] == 'green':
		# alien['color'] = 'yellow'
		# alien['speed'] = 'medium'
		# alien['points'] = 10
	# elif alien['color'] == 'yellow':
		# alien['color'] = 'red'
		# alien['speed'] = 'fast'
		# alien['points'] = 15

# for alien in aliens[:5]:
	# print(alien)
# print("...")

# print(f"Total number of aliens: {len(aliens)}")



# pizza = {
    # 'crust': 'thick',
    # 'toppings': ['mushrooms', 'extra cheese'],
    # }

# print(f"You ordered a {pizza['crust']}-crust pizza "
    # "with the following toppings:")

# for topping in pizza['toppings']:
	# print("\t" + topping)


# favorite_languages = {
    # 'jen': ['python', 'ruby'],
    # 'sarah': ['c'],
    # 'edward': ['ruby', 'go'],
    # 'phil': ['python', 'haskell'],
    # }

# for name, languages in favorite_languages.items():
	# print(f"\n{name.title()}'s favorite languages are:")
	# for language in languages:
		# print(f"\t{language.title()}")


# users = {
    # 'aeinstein': {
        # 'first': 'albert',
        # 'last': 'einstein',
        # 'location': 'paris',
        # },
    
    # 'mcurie': {
        # 'first': 'marie',
        # 'last': 'curie',
        # 'location': 'paris',
        # },
    # }

# for username, user_info in users.items():
	# print(f"\nUsername: {username}")
	# full_name = f"{user_info['first']} {user_info['last']}"
	# location = user_info['location']
	
	# print(f"\tFull name: {full_name.title()}")
	# print(f"\tLocation: {location.title()}")

# tom = {'cat':'bob'}
# jerry = {'mouse':'frodo'}
# spike = {'dog':'sam'}

# pets = [tom, jerry, spike]
# for pet in pets:
	# print(pet)


# favplaces = {
    # 'zoo':'arya',
    # 'school':'cersei',
    # 'home':'bruce',
    # }
# for place, places in favplaces.items():
	# print(f"{places.title()}'s favorite place is {place}.")


# cities = {'ssc':{'country':'us', 'population': 15000, 'fact':'birthplace'},
    # 'omaha':{'country':'usa', 'population': 50000, 'fact':'south of me'},
    # 'lincoln':{'country':'united states', 'population': 70000, 'fact':'capital'}
    # }
# for city, town in cities.items():
	# print(f"\n{city.title()}:")
	# for x in town:
		# print(f"\t{x.title()}: {town[x]}")


