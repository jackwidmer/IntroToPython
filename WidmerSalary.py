yearsEmployed = input('For how many years have you been employed?: ')
yearsEmployed = int(yearsEmployed)

numOfChildren = input('How many children do you have?')
numOfChildren = int(numOfChildren)

monthlyWage = 400

experiencePay = 20 * yearsEmployed

childPay = 30 * numOfChildren

total = monthlyWage + experiencePay + childPay

print('The total amount is',total,'dollars.',monthlyWage,'dollars +',experiencePay,'dollars for',yearsEmployed,'years experience +',childPay,'dollars for',numOfChildren,'kids.')
