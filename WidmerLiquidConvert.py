#Ask the user which way they want to convert
#if they want to convert from g to l then do that
#if they want to convert l to g then do that

def GtoL():
    #prompt the user to enter an amount in gallons
    #program will convert to liters and display the result
    gallons = input("Enter an amount in gallons: ")
    gallons = float(gallons)
    liters = (gallons * 3.785)
    print(gallons , 'gallons is about',liters, 'liters!')
    return

def LtoG():
    #prompt the user to enter an amount in liters
    #program will convert to gallons and display the result
    liters = input("Enter an amount in liters: ")
    liters = float(liters)
    gallons = (liters / 3.785)
    print(liters , 'liters is about',gallons, 'gallons!') 
    return


##################################################################
#mainline

choice = input("Enter 'l' to convert gallons to liters, or 'g' for liters to gallons: ")
if choice == 'l':
    GtoL()
if choice == 'g':
    LtoG()

