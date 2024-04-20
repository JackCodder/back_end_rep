# Task 3
n = int(input('Введите число: '))

factorial = 1
for i in range(1, n+1):
    factorial *= i

print('факториал числа =', factorial)