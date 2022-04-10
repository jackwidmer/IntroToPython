#Jack Widmer, 9/16/2021, a miles-per-gallon calculator
strMiles = input('How many miles have you driven since the last time you filled up?: ')
fltMiles = float(strMiles)

strGallons = input('How many gallons are required to fill your tank?: ')
fltGallons = float(strGallons)

mpg = fltMiles / fltGallons

print('Your miles-per-gallon is',mpg)
