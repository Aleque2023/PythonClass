###Alex Quezada, 8/11/2023, Module 3 Assignment
###Calculating the cost to install fiber optic

print("Welcome to my program!")
Taxes = .07
Company = input("What is the name of your company: ")
Fiber = float(input("How many feet of fiber optic cabling will " + Company + " require to be installed: "))
Cost = Fiber * .87
Total_Cost = str((Cost * Taxes) + Cost)
Cost = str(Cost)
print("The cost for " + Company + " will be $" + Cost + " excluding taxes.")
print("The total cost for " + Company + " will be $" + Total_Cost + " including taxes.")
print("Thanks for using my program!!!")
