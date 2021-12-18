from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        numeric_list = [num for num in (*args, *kwargs.values())]
        a = [f'{func.__name__}({num}: {type(num)})' for num in numeric_list]
        print(*a, *func(*args, **kwargs), sep=',\n')
    return wrapper


@type_logger
def cube_calculation(*x, **y):
    numeric_list = [num for num in (*x, *y.values()) if isinstance(num, int) or isinstance(num, float)]
    return [k ** 3 for k in numeric_list]

# c = cube_calculation(3, 9, 3.3, 10, 13)
c = cube_calculation(3, {'element': 3}, (5, 'letter'))