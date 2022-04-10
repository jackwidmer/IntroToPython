import time
temp = 80
furnaceState = False

while True:
    print("Hello")
    time.sleep(2)
    if (temp < 65) and (furnaceState == False):
        print("turn the furnace on")
        furnaceState = True
    if (temp > 65) and (furnaceState == True):
        print("turn the furnace off")
        furnaceState = False
        print(furnaceState)
        print(temp)

print("this program is over")


#
