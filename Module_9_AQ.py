###Alex Quezada, 9/24/2023, Module 9 Assignment
###Creating a banking program with classes

#The main goal is for it to print a message if it is below the minimum balance
while True: #Since we want to run this program with the balance being at two different values, I made a while loop
	try:
		cbalance = float(input("What is your balance: "))
	except:
		print("\nNot valid.\n")
		continue
	class BankAccount(): #The parent class
	
		def __init__(self, accountNumber, balance):
		
			self.accountNumber = accountNumber
			self.balance = balance
			
		def withdrawl(self):
			return
			
		def deposit(self):
			return
			
		def getBalance(self):
			return self.balance


	class Checking(BankAccount): #The 1st child class
		
		def __init__(self, accountNumber, balance, fees, minimum_balance):
			super().__init__(accountNumber, balance)
			
			self.fees = fees
			self.minimum_balance = minimum_balance
		
		def deductfees(self):
			return self.balance - self.fees
		
		def checkMinimumBalance(self, balance):
			try:
				if self.balance < self.minimum_balance or checkingAccount.deductfees() < self.minimum_balance:
					print("Your account is below the minimum balance! ")
			except:
				pass
			
			
	class Saving(BankAccount): #The 2nd child class
		
		def __init__(self, accountNumber, balance, interestRate):
			super().__init__(accountNumber, balance)
			
			self.interestRate = interestRate
			
		def addinterest():
			self.balance += (self.interestRate * self.balance)
			
	try:
		checkingAccount = Checking(1, cbalance, 5, 50) #Object 1
		print(f"Your Checking balance was reduced by ${checkingAccount.fees} it is now ${checkingAccount.deductfees()}.")
		checkingAccount.checkMinimumBalance(cbalance)
		savingsAccount = Saving(2, 25, .02) #Object 2
	except:
		pass
	try:
		choice = input("Type 'quit' if you wish to leave the program: ")
		if choice == 'quit':
			break
	except:
		pass
