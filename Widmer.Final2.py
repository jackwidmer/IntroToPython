# Jack Widmer
###########################################################################
#1  Ask the user to enter his annual income.  Add $600 to this amount to reflect
# a COVID payment from the government.  Print out "Your new annual income is:"
# followed by the new total amount.
print('#1 Ask the user to enter his annual income, add to it, print the result')
annualIncome = input("Please enter your annual income: ")
annualIncome = int(annualIncome)
totalIncome = annualIncome + 600
totalIncome = str(totalIncome)
print("Your new annual income is:",totalIncome)

###########################################################################
#2 Import the Module needed do math. As the user to enter a number.
# Calculate the square root of that number and print out the result.
print('#2 Import a Module.')
import math
x = input("Please enter a number: ")
x = int(x)
print(math.sqrt(x))

###########################################################################
#3 Using the Random function.
#Using a For Loop, print 10 random intergers between the values of 1 and 100.
print('3 Using the Random function')
import random
for y in range(10):
    print(random.randint(1,100))

###########################################################################
#4 Area of a Circle
print('4 Area of a Circle')
#Prompt the user to enter the radius and
#print a nice message back to the user with the answer.
radius = input("Please enter the Radius of the circle: ")
radius = int(radius)
area = (math.pi) * (radius**2)
print("The area of the circle is:",area,"Nice!")

###########################################################################

#5 Area of a Rectangle
print('5 Area of a Rectangle')
#Write a program that will compute the area of a rectangle.
#Prompt the user to enter the width and height of the rectangle.
#Print a nice message with the answer
width = input("Please enter the width of your rectangle: ")
width = int(width)
height = input("Please enter the height of your rectangle: ")
height = int(height)
rectArea = width * height
print("The area of the rectangle is:",rectArea,"You are beautiful!")

###########################################################################
#6 Add/Subtract Two Numbers
print('6  Add/Subtract Two Numbers')
# Write a program that can either add or subtract two numbers.
#You should first ask the user whether they want to add or subtract,
#then take in the two numbers, then finally perform
#the required operation and print the result.
plusMinus = input("Do you want to add (a) or (s) subtract?: ")
if plusMinus == 'a':
    firstAdd = input("Please enter your first number: ")
    firstAdd = int(firstAdd)
    secondAdd = input("Please enter your second number: ")
    secondAdd = int(secondAdd)
    add = firstAdd + secondAdd
    print(add)
if plusMinus == 's':
    firstSub = input("Please enter your first number: ")
    firstSub = int(firstSub)
    secondSub = input("Please enter your second number: ")
    secondSub = int(secondSub)
    subtract = firstSub - secondSub
    print(subtract)

###########################################################################
#7 While Loop
print('7 - Use While Loop to print numbers from 1 to 5')
z = 1
while(z <= 5):
    print(z)
    z += 1
##########################################################################
#8 For Loop:  Count Down
#8 Use a For Loop to count down from 10 to 1, then prints 'Boom'.
print ('8 - Use For loop to countdown from 10 to 1')
count = 1
for count in range(10,0, -1):
    print(count)
print('Boom')
###########################################################################
#9 While  Loop:  Count Down
#9 Use a While Loop to count down from 10 to 1, then prints 'Boom'.
print ('9 - Use While loop to countdown from 10 to 1')
countTwo = 10
while countTwo > 0:
    print(countTwo)
    countTwo = countTwo -1
print('Boom')

