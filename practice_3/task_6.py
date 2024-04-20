# Task 6
n = int(input('Введите число: '))
cnt = 0

while n > 0:
    cnt += 1
    n //= 10

print('Количество цифр в числе =', cnt)