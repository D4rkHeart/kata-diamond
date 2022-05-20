space = " "
letter = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
selChar = input("Enter the letter that will define the size of the diamond: ")

#Verification of the user input
try:
	x = letter.index(selChar)
except:
	print("Please use only capital letter") 
	exit()

#Print de upper part of the diamond
print(space*(x) + "A")
for y in range(1, x + 1, 1):
	print(space*(x-y) + letter[y] + space*((y*2)-1) + letter[y])

#Print de lower part of the diamond
for y in range(x -1 ,0, -1):
	print(space*(x-y) + letter[y] + space*((y*2)-1) + letter[y])
print(space*(x) + "A")