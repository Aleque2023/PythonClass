###Alex Quezada, 8/28/2023, Module 5 Assignment
###Calculating the cost to install fiber optic with If statements

print("Welcome to my program!")
Taxes = .07                                              #Programs shouldn't evade taxes
Company = input("What is the name of your company: ")
Fiber = float(input("How many feet of fiber optic cabling will " + Company + " require to be installed: "))
if Fiber > 100 and Fiber <= 250:                         #It will cost .80 per foot if the amount of feet is from 101-250
	Cost = Fiber * .80
	print("New total for each foot is .80")
elif Fiber > 250 and Fiber <= 500:                       #It will cost .70 per foot if the amount of feet is from 251-500
	Cost = Fiber * .70
	print("New total for each foot is .70")
elif Fiber > 500:                                        #It will cost .50 per foot if the amount of feet is 501+
	Cost = Fiber * .50
	print("New total for each foot is .50")
else:                                                    #If it is less than 101, then no discount is applied
	Cost = Fiber * .87
	print("No discount applied")
Total_Cost = str(round((Cost * Taxes) + Cost,2))
Cost = str(round(Cost, 2))
print("The cost for " + Company + " will be $" + Cost + " excluding taxes.")
print("The total cost for " + Company + " will be $" + Total_Cost + " including taxes.")
print("Thanks for using my program!!!")

