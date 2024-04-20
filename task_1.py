# Task 1
n = int(input('Введите число: '))
n_copy = n

# цикл while:
total_1 = 0
k = 1

while n > 0:
    if k % 2 == 0:
        total_1 += k

    k += 1
    n -= 1

print('Сумма четных чисел при помощи цикла while =', total_1)

# цикл for:
total_2 = 0

for i in range(2, n_copy+1, 2):
    total_2 += i

print('Сумма четных чисел при помощи цикла for =', total_2)