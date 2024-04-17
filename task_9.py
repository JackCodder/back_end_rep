#Task 9

lst_1 = [1, 2, 3, 5]
lst_2 = [5, 6, 1, 7, 8]

lst = list(set(lst_1 + lst_2)) #соединение и удаление повторяющихся элементов  

lst.sort()

print(lst)
