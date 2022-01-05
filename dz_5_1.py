import sys

n = int(input('Введите любое число: '))

nums_gen_1 = (n for n in range(1, n + 1, 2))

print(*nums_gen_1, sep=', ')

"""
Посмотрел класс и размер  
"""
print(type(nums_gen_1), sys.getsizeof(nums_gen_1))








