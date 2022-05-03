#Password Help
import random 

#List for lowercase letters, uppercase letters, numbers, and special characters
lowercaseL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specialCharacters = ['!', '@', '#', '$', '%', '&', '*']

#joins list together into one variable, to use after the user answers the promt
onlyLetters = lowercaseL + uppercaseL
lowercaseandNum = lowercaseL + numbers
LettersandNumbers = lowercaseL + uppercaseL + numbers
allLandN = lowercaseL + uppercaseL + numbers + specialCharacters
lowercaseandSC = lowercaseL + specialCharacters
lowercaseSCandNum = lowercaseL + specialCharacters + numbers

#creates and empty list for the passwords after generated 
Savedpasswords = []

#Introduction to Password Help
print("Hello! Welcome to 'Password Help'!")
print("If you constantly need to come up with new passwords, this is for you!")

#Function for password prompt
#Asks user a series of question to figure out what kind of password to generate and what length
def passwordPromt():

	capitals = input("Does your password require capital letters?(Y/N): ")
	numRequirement = input("Does your password require numbers?(Y/N): ")
	scRequirement = input("Does your password require special characters?(Y/N): ")
	length = int(input("How long do you want your password?(We recommend 8 or above): "))

	#Condition for when password has no capitals, numbers or special characters 
	#In each if/elif statement, the new password will be created based on the conditions as well as adding the password to "Savedpasswords"
	if capitals=='N' and numRequirement=='N' and scRequirement=='N':
		newPassword = random.sample(lowercaseL, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Condition for when password has capitals, but no numbers or special characters 
	elif capitals=='Y' and numRequirement=='N' and scRequirement=='N':
		newPassword = random.sample(onlyLetters, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Condition for when password has capitals and numbers, but no special characters 
	elif capitals=='Y' and numRequirement=='Y' and scRequirement=='N':
		newPassword = random.sample(LettersandNumbers, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Condition for when password has capitals, numbers, and special characters 
	elif capitals=='Y' and numRequirement=='Y' and scRequirement=='Y':
		newPassword = random.sample(allLandN, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Condition for when password has numbers, but no special characters and no capitals  
	elif capitals=='N' and numRequirement=='Y' and scRequirement=='N':
		newPassword = random.sample(lowercaseandNum, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Condition for when password has special characters but no numbers and no capitals 
	elif capitals=='N' and numRequirement=='N' and scRequirement=='Y':
		newPassword = random.sample(lowercaseandSC, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Condition for when password has numbers and special characters, but no capitals 
	elif capitals=='N' and numRequirement=='Y' and scRequirement=='Y':
		newPassword = random.sample(lowercaseSCandNum, length)
		password = "".join(newPassword)
		Savedpasswords.append(password)
		print(password)

	#Prints Savedpasswords list
	print("Current saved passwords: ",Savedpasswords)

#calls passwordPromt function
passwordPromt()

#Asks the user if they want to generate another password, if yes then the function will be called again to repeat the promt
retry = input("Would you like to create another password?(Y/N): ")
if retry == 'Y':
	passwordPromt()
	retry = input("Would you like to create another password?(Y/N): ")
	passwordPromt()
else:
	print("Goodbye!")





