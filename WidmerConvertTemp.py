#Ask user which way they want to convert
request = input("Enter 'f' to convert celsius to farenheit, or 'c' for farenheit to celsius: ")
if request == 'c':
    


#prompt the user to enter a temp in farenheit
#program will convert to celcius and display the result

    ftemp = input("Enter a temperature in farenheit: ")
    fTemp = float(ftemp)
    cTemp = (fTemp - 32) * 5/9
    print(ftemp , 'degrees in farenheit is',cTemp, 'degrees in celsius!')

#prompt the user to enter a temp in celsius
#program will convert to farenheit and display the result

if request == 'f':
    ctemp = input("Enter a temperature in celsius: ")
    cTemp = float(ctemp)
    fTemp = (cTemp * 9/5) + 32
    print(ctemp , 'degrees in celsius is',fTemp, 'degrees in farenheit!') 
