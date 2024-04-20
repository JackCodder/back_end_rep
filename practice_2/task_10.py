#Task 10

lst = list(map(int, input('Введите последовательность чисел: ').split()))

print(len(lst) == len(set(lst)))
#True - уникальна последовательность
#False - неуникальна последовательность