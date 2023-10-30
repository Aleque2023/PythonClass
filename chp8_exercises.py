# def testfunc():
	# print("Hello Python World!")
	


# testfunc()

# testfunc()

# testfunc()



# def printusername(name):
	# print(f'The user name is {name.title()}.')


# print()

# printusername('tommy')
# print()
# printusername('cindy')
# print()
# printusername('luke')
# print()
# printusername('charlotte')


# def printnumber(value):
	# print(f'The number is: {value}.')

# numvalue1 = 33
# numvalue2 = 44

# print()
# printnumber(777)
# print()
# printnumber(888)
# print()

# printnumber(numvalue1)
# print()
# printnumber(numvalue2)
# print()





# def printworldserieswinners(year, team):
	# print(f'The {team.title()} won the {year} World Series.')

# printworldserieswinners(2004, 'Red Sox')
# printworldserieswinners(2007, 'Giants')



# def printwseries(team, year):
	# print(f'The {team.title()} won the {year} World Series.')

# printwseries(team='red sox', year=2004)
# printwseries(team='white sox', year=2005)
# printwseries(team='cardinals', year=2006)

# printwseries(year=2011, team='cardinals')
# printwseries(year=2012, team='giants')
# printwseries(year=2013, team='red sox')

# printwseries('cardinals', year=2006)
# #printwseries(team='red sox', 2004) #will not work because it does not have year= with the integer 2004
# #printwseries(2011, team='cardinals') #will not work because the year does not have year= and it is in the team spot instead of the year one
# #printwseries(team='red sox', 2004) #will not work because it does not have year= with the integer 2004
# # printwseries(year=2013, 'red sox') #will not work because it does not have team= with the string red sox




# def winners(team, year=1900):
	# print(f'The {team.title()} won the {year} World Series.')

# winners('red sox')
# winners('white sox')

# winners(team='cardinals')
# winners(team='giants')

# winners(team='red sox', year=2004)
# winners(team='white sox', year=2005)
# winners(team='cardinals', year=2006)

# winners(year=2011, team='cardinals')
# winners(year=2012, team='giants')
# winners(year=2013, team='red sox')





# def concatenationofstrings(param_01, param_02):
	# returnstring = f'{param_01} {param_02}'
	# return returnstring.title()

# print(concatenationofstrings('tom', 'johnson'))
# print(concatenationofstrings('sue', 'wilson'))


# def test(param1, param2, param3=''):
	# if param3:
		# returnstring = f'{param1} {param2} {param3}'
	# else:
		# returnstring = f'{param1} {param2}'
	# return returnstring.title()

# firstname1 = 'mary'
# middlename1 = 'mark'
# lastname1 = 'carter'

# firstname2 = 'larry'
# lastname2 = 'wilson'

# firstname3 = 'anna'
# middlename3 = 'leek'
# lastname3 = 'giles'

# print(test(firstname1, middlename1, lastname1))
# print(test(firstname2, lastname2))
# print(test(firstname3, middlename3, lastname3))

# output1 = test(firstname1, middlename1, lastname1)
# print(output1)

# output1 = test(firstname2, lastname2)
# print(output1)

# output1 = test(firstname3, middlename3, lastname3)
# print(output1)



# def dictionary(para1, para2):
	# returndict = {'firstname': para1, 'lastname': para2}
	# return returndict

# firstname01 = 'mary'
# lastname01 = 'carter'

# firstname02 = 'larry'
# lastname02 = 'wilson'

# output = dictionary('anna', 'giles')
# print(output)

# output = dictionary(firstname01, lastname01)
# print(output)

# print(dictionary(firstname02, lastname02))

# def mylist(teamlist):
	
	# for team in teamlist:
		# print(f'A popular sports team is the {team.title()}.')

# baseballteam = ['cardinals', 'tigers', 'red sox', 'rangers', 'cubs']

# footballteam = ['chiefs', 'packers', 'cowboys']

# mylist(baseballteam)
# print()
# mylist(footballteam)
# print()

# import math
# print(math.pi)


# def display_message():
	# print("I am learning about functions!")

# display_message()



# def favbook(title):
	# print(f"One of my favorite books is {title.title()}!")

# favbook(input("What is your favorite book? "))


# def buildperson(firstname, lastname):
	# person = {'first': firstname, 'last': lastname}
	# return person
	
# musician = buildperson('jimi', 'hendrix')
# print(musician)


# def buildperson(firstname, lastname, age=None):
	# person = {'first': firstname, 'last': lastname}
	# if age:
		# person['age']=age
	# return person
	
# musician = buildperson('jimi', 'hendrix', age=27)
# print(musician)


# mes = ['hi there', 'what is up', 'hey', 'bro']

# def play(total):
	# for tot in total:
		# print(tot)

# play(mes)


# mes = ['hi there', 'what is up', 'hey', 'bro']
# newmes = []
# def play(total):
	# for tot in total:
		# newmes.append(tot)
		# print(tot)
		# mes.remove(tot)

# play(mes)

# print(f"\n{mes}\n")
# print(newmes)

##Need chp9_exercises file open
from chp9_exercises import test, bruh as b

test()
b()


import chp9_exercises as d

d.test()
d.bruh()n

