# Task 9
lst = ['Hello', 'IT_CODE', 'abracadabra', 'Python', 'Java', 'C++', 'IT_CODE', 'Java']
# lst = input().split()
lst_copy = lst

# цикл while:
k = 0

while k < len(lst):
    if lst.count(lst[k]) > 1:
        del lst[k]
    k += 1

print('при помощи цикла while =', lst)

# цикл for:
cnt = 0

for item in lst_copy:
    if lst_copy.count(item) > 1:
        del lst_copy[item]

print('при помощи цикла for =', lst_copy)
