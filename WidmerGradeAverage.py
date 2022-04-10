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

print('Your average grade is',gradeAverage)
