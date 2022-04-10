inputName = input("Please enter your full name: ")
strName = str(inputName)

allCaps = strName.upper()
capstoString = str(allCaps)

allLower = strName.lower()
lowertoString = str(allLower)

count = len(strName) - strName.count(" ")
countString = str(count)

print("Here's your name in all caps: " + capstoString + ".")
print("Here's your name in all lower case: " + lowertoString + ".")
print("You have " + countString + " characters in your name!")
