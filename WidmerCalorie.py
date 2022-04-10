#Jack Widmer
#10/12/21
#Program: Calorie
#This program will inform the suggested daily calories of food consumption for an individual

gender = input("Please enter your gender (c for child, m for Male, f for Female): ")
age = input("Please enter your age: ")
age = int(age)
alevel = input("please enter your activity level(s for Sedentary, m for Moderately Active, a for Active): ") 

print(gender)
print(age)
print(alevel)

#child

if ((age == 2) or (age == 3)) and (gender == 'c') and (alevel == 's'):
    print("You need 1000 calories!")

if ((age == 2) or (age == 3)) and (gender == 'c') and ((alevel == 'm') or (alevel == 'a')):
    print("You need 1000 to 1400 calories!")
    
#female 4-8
    
if (gender=='f') and ((age >= 4) and (age <=8 )) and (alevel=='s'):
    print('You should consume 1200 calories per day!')
    
if (gender=='f') and ((age >= 4) and (age <=8 )) and (alevel=='m'):
    print('You should consume 1,400-1,600 calories per day!')
    
if (gender=='f') and ((age >= 4) and (age <= 8)) and (alevel=='a'):
    print('You should consume 1,400-1,800 calories per day!')
    
#female 9-13
    
if (gender=='f') and ((age >= 9) and (age <=13 )) and (alevel=='s'):
    print('You should consume 1,600 calories per day!')
    
if (gender=='f') and ((age >= 9) and (age <=13 )) and (alevel=='m'):
    print('You should consume 1,600-2,000 calories per day!')
    
if (gender=='f') and ((age >= 9) and (age <=13 )) and (alevel=='a'):
    print('You should consume 2,000 calories per day!')

#female 14-18
    
if (gender=='f') and ((age >= 14) and (age <=18)) and (alevel=='s'):
    print('You should consume 1,800 calories per day!')
    
if (gender=='f') and ((age >= 14) and (age <=18 )) and (alevel=='m'):
    print('You should consume 2,000 calories per day!')
    
if (gender=='f') and ((age >= 14) and (age <=18 )) and (alevel=='a'):
    print('You should consume 2,400 calories per day!')

#female 19-30

if (gender=='f') and ((age >= 19) and (age <=30 )) and (alevel=='s'):
    print('You should consume 2,000 calories per day!')

if (gender=='f') and ((age >= 19) and (age <=30 )) and (alevel=='m'):
    print('You should consume 2,000 - 2,200 calories per day!')

if (gender=='f') and ((age >= 19) and (age <=30 )) and (alevel=='a'):
    print('You should consume 2,400 calories per day!')

#female 31-50

if (gender=='f') and ((age >= 31) and (age <=50 )) and (alevel=='s'):
    print('You should consume 1,800 calories per day!')

if (gender=='f') and ((age >= 31) and (age <=50 )) and (alevel=='m'):
    print('You should consume 2,000 calories per day!')

if (gender=='f') and ((age >= 31) and (age <=50 )) and (alevel=='a'):
    print('You should consume 2,200 calories per day!')

#female 51+

if (gender=='f') and (age >= 51) and (alevel=='s'):
    print('You should consume 1,600 calories per day!')

if (gender=='f') and (age >= 51) and (alevel=='m'):
    print('You should consume 1,800 calories per day!')

if (gender=='f') and (age >= 51) and (alevel=='a'):
    print('You should consume 2,000-2,200 calories per day!')

#male 4-8
    
if (gender=='m') and ((age >= 4) and (age <=8 )) and (alevel=='s'):
    print('You should consume 1400 calories per day!')
    
if (gender=='m') and ((age >= 4) and (age <=8 )) and (alevel=='m'):
    print('You should consume 1,400-1,600 calories per day!')
    
if (gender=='m') and ((age >= 4) and (age <= 8)) and (alevel=='a'):
    print('You should consume 1,600-2,000 calories per day!')
    
#male 9-13
    
if (gender=='m') and ((age >= 9) and (age <=13 )) and (alevel=='s'):
    print('You should consume 1,800 calories per day!')
    
if (gender=='m') and ((age >= 9) and (age <=13 )) and (alevel=='m'):
    print('You should consume 1,800-2,200 calories per day!')
    
if (gender=='m') and ((age >= 9) and (age <=13 )) and (alevel=='a'):
    print('You should consume 2,000-2600 calories per day!')

#male 14-18
    
if (gender=='m') and ((age >= 14) and (age <=18)) and (alevel=='s'):
    print('You should consume 2,200 calories per day!')
    
if (gender=='m') and ((age >= 14) and (age <=18 )) and (alevel=='m'):
    print('You should consume 2,400-2,800 calories per day!')
    
if (gender=='m') and ((age >= 14) and (age <=18 )) and (alevel=='a'):
    print('You should consume 2,800-3,200 calories per day!')

#male 19-30

if (gender=='m') and ((age >= 19) and (age <=30 )) and (alevel=='s'):
    print('You should consume 2,400 calories per day!')

if (gender=='m') and ((age >= 19) and (age <=30 )) and (alevel=='m'):
    print('You should consume 2,600 - 2,800 calories per day!')

if (gender=='m') and ((age >= 19) and (age <=30 )) and (alevel=='a'):
    print('You should consume 3000 calories per day!')

#male 31-50

if (gender=='m') and ((age >= 31) and (age <=50 )) and (alevel=='s'):
    print('You should consume 2,200 calories per day!')

if (gender=='m') and ((age >= 31) and (age <=50 )) and (alevel=='m'):
    print('You should consume 2,400-2,600 calories per day!')

if (gender=='m') and ((age >= 31) and (age <=50 )) and (alevel=='a'):
    print('You should consume 2,800-3,000 calories per day!')

#male 51+

if (gender=='m') and (age >= 51) and (alevel=='s'):
    print('You should consume 2,000 calories per day!')

if (gender=='m') and (age >= 51) and (alevel=='m'):
    print('You should consume 2,000-2,400 calories per day!')

if (gender=='m') and (age >= 51) and (alevel=='a'):
    print('You should consume 2,400-2,800 calories per day!')


    
