# Jack Widmer
# WidmerFunctionsSamples.py
# Week 12   11/9/21

def getIpAddress(interfaceIndex):
    firstIp = '192.45.68'
    secondIp = '127.0.0.1'
    thirdIp = '65.81.29.32'
    if interfaceIndex == '1':
        return firstIp
    if interfaceIndex == '2':
        return secondIp
    if interfaceIndex == '3':
        return thirdIp




########Main line##############
interfaceIndex = input('Please enter an interface index of 1, 2, or 3: ')
ip = getIpAddress(interfaceIndex)

print('The IP Address is',ip)
