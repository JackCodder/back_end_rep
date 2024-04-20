# Task 4
lst = ['Hello', 'IT_CODE', 'abracadabra', 'Python', 'Java', 'C++']
# lst = input().split()

for index, value in enumerate(lst):
    if index % 3 == 0:
        print(index, value)