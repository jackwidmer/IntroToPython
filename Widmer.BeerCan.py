inputCans = input("How many ounces of aluminum beer cans have you saved in your shed?: ")

ounces = int(inputCans)
strOunces = str(inputCans)
pounds = ounces / 16
strPounds = str(pounds)
tons = pounds / 2000
strTons = str(tons)

print("You have " + strOunces + " ounces of beer cans.")
print("So, you have " + strPounds + " pounds of beer cans.")
print("And you have a whopping " + strTons + " tons of beer cans!")

