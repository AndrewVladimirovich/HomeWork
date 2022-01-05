"""
Клон сделал по примеру из урока
"""
list_of_numerics = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

dictionary_1 = {i: 0 for i in list_of_numerics}


for i in list_of_numerics:
    dictionary_1[i] += 1

print(dictionary_1)