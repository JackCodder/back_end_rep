#Task 10

lst = list(map(int, input('Введите последовательность чисел: ').split()))

print('уникальна последовательность' if len(lst) == len(set(lst)) else 'неуникальна последовательность')
