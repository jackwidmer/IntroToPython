#Jack Widmer

#1 Assign a string value to a variable. Print the variable.
print('#1')
x = 'hello'
print(x)

#2 Assign an integer value to a variable. Print the variable.
print('#2')
y = 45
print(y)

#3 Assign float value to a variable. Print the variable.
print('#3')
z = 5.6
print(z)

#4 Spacing Issues: fix the following code:
#someNumber = 4
#if someNumber > 3:
#print('Yeah, the number is bigger')
print('#4')
someNumber = 4
if someNumber > 3:
    print('Yeah, the number is bigger')
    
#5 Print the first three days of the week on one line.
print('#5')
print('Monday','Tuesday','Wednesday')

#6 Obtain the data type of the value 56.76
print('#6')
type(56.76)

#7
#Assign an integer to a variable. Convert that variable to a string.
#Store that string back in the x variable
print('#7')
x = 46
x = str(x)

#8
#print the calculated value of 4+4
print(4+4)

#9
#print the calculated value of 4 times 5
print('#9')
print (4*5)

#10 Print the calculated value of 5 divided by 2 but with no remainder
print('#10')
print(5//2)

#11 Print the remainder of the calculated value of 5 divided by 2
print('#11')
print(5%2)

#12 Use a while loop to print numbers 1 to 15


temp = -3

if temp < -10:
    print("wear winter jacket")
elif temp < 15:
    print("wear long sleeve shirt")
else:
    print("wear t-shirt")

#13 Use a for loop to print numbers 1 to 15
print('#13')
for counter in range(1,16):
    print(counter)

#14 create a list that stores the days of the week using the 3 letter abbreviation
#Name the list days and print it.
print('#14')
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(days)

#15 From the previous list, extract the second day of the week and print it
print(days[1])

#16 Define a function f1, which will print your name
#Call the function
print('#16')
def f1():
    print('Jack Widmer')
    return
#############################
f1()

#17 Define a function f2, which will receive a string as an argument.
#The function will then print the received string.
#The function will not return any values
#Call the function
print('#17')
def f2(x):
    print(x)
    return
#######################
f2('jack')

#18 Define a function f3
#The function will return your name
#The function will not receive any values
#Call the function. Print the value the function has returned
print('#18')
def f3():
    return 'jack'
##########################
x = f3()
print(x)

#19 Define a function f4
#Function will return a calculated paycheck
#You will pass the function your base pay. an integer value of 500.
#The function will add 300 hardship covid pay to that base pay
#The function will return the total pay
#Call the function and print the returned value
print('#19')
def f4(basePay):
    totalPay = basePay + 300
    return totalPay
#################
x = f4(500)
print(x)
