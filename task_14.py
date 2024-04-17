#Task 14

array = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55]
    ]

array_trnsp = []

for i in range(len(array)):
    array_basic = []
    for j in range(len(array[i])):
        array_basic.append(array[j][i])
    array_trnsp.append(array_basic)

for i in array_trnsp:
    print(i)

