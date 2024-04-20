#Task 13

students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print('Спсобо №1')
print(students | employees, students & employees, employees - students, employees ^ students, sep='\n')


print('Спсобо №2')
print(students.union(employees), students.intersection(employees), employees.difference(students), employees.symmetric_difference(students), sep='\n')
