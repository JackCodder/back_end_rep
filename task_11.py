# Task 11

week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

print(*week)

for i in range(1, 32):
    if i % 7 == 0:
        print(i, end='\n')
    elif i > 9:
        print(i, end=' ')
    else:
        print(i, end='  ')