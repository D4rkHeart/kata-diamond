space = " "
letter = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
selChar = input("Enter the letter that will define the size of the diamond: ")

#Verification of the user input
try:
	x = letter.index(selChar)
except:
	print("Please use only capital letter") 
	exit()
