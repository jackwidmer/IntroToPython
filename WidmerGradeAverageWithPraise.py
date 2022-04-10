import statistics
print('Please enter your grades for the following classes(Grades range from 0-10):')
geometryGrade = input('Geometry: ')
geometryGrade = int(geometryGrade)

algebraGrade = input('Algebra: ')
algebraGrade = int(algebraGrade)

physicsGrade = input('Physics: ')
physicsGrade = int(physicsGrade)

grades = [geometryGrade, algebraGrade, physicsGrade]

gradeAverage = statistics.mean(grades)

if gradeAverage >= 7:
    print('Your average grade is',gradeAverage,'Good Job!')
if gradeAverage == 5:
    print('Your average grade is',gradeAverage,', you need to work harder!')
if gradeAverage <=4:
    print('Your average grade is',gradeAverage,'. FAILURE. YOU REALLY NEED TO STEP IT UP.')
