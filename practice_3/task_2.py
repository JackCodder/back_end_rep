# Task 2
array = ['Hello', 'IT_CODE', 'abracadabra']
# array = input().split()

# цикл while:
mx_word_1 = ''
k = 0

while k < len(array):
    if len(array[k]) >= len(mx_word_1):
        mx_word_1 = array[k]

    k += 1
print('Самое длинное слово при помощи цикла while =', mx_word_1)

# цикл for:
mx_word_2 = ''

for word in array:
    if len(word) >= len(mx_word_2):
        mx_word_2 = word

print('Самое длинное слово при помощи цикла for =', mx_word_2)