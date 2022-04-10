# JACK WIDMER
###########################################################################
#1  Assign a string value to a variable. Print the variable.
print('#1 Assign a string value to a variable. Print the variable')
a = 'Hello!'
print(a)
###########################################################################
#2 Assign an integer value to a variable. Print the variable.
print('#2 Assign an integer value to a variable. Print the variable.')
z = 5
print(z)
###########################################################################
#3 Assign float value to a variable. Print the variable
print('3 Assign float value to a variable. Print the variable')
y = 6.7
print(y)
###########################################################################
#4
print('4 spacing issues: fix the following 3 lines of  code')
#spacing issues: fix the following 3 lines of  code. You will need to first remove
# the three comment characters at the beginning of each line.
some_number = 4
if some_number > 3:
    print("Yeah, the number is bigger.")
###########################################################################

#5 Print the five  days of the week on one line
print('5 Print the five  days of the week on one line')
print('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
###########################################################################
#6
print('6  Obtain the data type of the value  56.76')
# Obtain the data type of the value  56.76
print(type(56.76))
###########################################################################
#7
print('7')
print('assign an integer to a variable.  Convert that variable to a string and')
print(' store that string back in the x variable.')
x = 70
x = str(x)
###########################################################################
#8
print('8 print the calculated value of 4 + 4')
# print the calculated value of 4 + 4
print(4+4)
###########################################################################
#9
print('9 print the calculated value of 4  times 5')
# print the calculated value of 4  times 5
print(4*5)
###########################################################################
#10
print('10 print the calculated value of 5 divided 2 but with no remainder')
# print the   calculated value of 5 divided 2 but with no remainder
print(5//2)

###########################################################################
#11
# print the remainder only of the calculated value of 5 divided 2
print ('11 print the remainder only of the calculated value of 5 divided 2')
print(5%2)


###########################################################################
#12
print('#12 use a while loop to print the numbers from 1 to 15')
#use a while loop to print the numbers from 1 to 15
counter = 1
while counter < 16:
    print(counter)
    counter = counter + 1

###########################################################################
#13
print('#13 use a for loop to print the numbers from 1 to 15')
#use a for loop to print the numbers from 1 to 15
for counter in range(1,16):
    print(counter)

###########################################################################
#14
print('#14')  
# create a  create a list that stores the days of the week using the 3 letter abbreviation.list that stores the days of the week using the 3 letter abbreviation.
# name the list days. Print the list.
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(days)

###########################################################################
#15
print('#15 From the previous list, extract the second day of the week and print it')
# From the previous list, extract the second day of the week and print it.
print(days[1])

###########################################################################
#16
print('16 Define a function f1')
# Define a function f1, which will print your name.
# Call the function.
def f1():
    print('Jack Widmer')
    return

f1()
###########################################################################
#16
print('16 Define a function f2')
# Define a function f2, which will receive a string as an arguement.
# The function will then print that received string.
# The function will not return any values.
# Call the function, passing it your name.
def f2(b):
    print(b)
    return

f2('Jack Widmer')
############################################################################
#17
print('17 Define a function f3.')
# Define a function f3.
# The function will return your name.That is all it does.
# You will not pass the function any values.
# Call the function.  Afterwards, print the value function has returned.
def f3():
    return 'Jack Widmer'

c = f3()
print(c)
###########################################################################
#18
print('18 Define a function f4')
# Define a function f4.
# The function will return a calculated paycheck
# You will  pass the function your base pay, an integer value of 500.
# The function will add 300 hardship covid pay to that base pay.
# The function will return total pay.
# Call the function.  Afterwards, print the value function has returned.
def f4(basePay):
    total = basePay + 300
    return total

d = f4(500)
print(d)









