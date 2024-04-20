# Task 8
lst = ['Hello', 'IT_CODE', 'abracadabra', 'Python', 'Java', 'C++', 'IT_CODE']
# lst = input().split()

print('Список не содержит дубликатов' if len(lst) == len(set(lst)) else 'Список содержит дубликаты')