"""
Клон сделал по примеру из урока
"""
list_of_numerics = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

numerics_more_than_previous = [list_of_numerics[num] for num in range(1, len(list_of_numerics)) if list_of_numerics[num] > list_of_numerics[num - 1]]

print(numerics_more_than_previous)

