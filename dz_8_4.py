from functools import wraps

def value_verify(k_function):
    def _value_verify(function):

        @wraps(function)
        def wrapper(num):
            if k_function(num):
                print(function(num))
            else:
                raise ValueError(f'wrong value: {num}')

        return wrapper
    return _value_verify

@value_verify(lambda x: x > 0)
def cube_calculation(x):
    return x ** 3

try:
    a = cube_calculation(5)
    print(help(cube_calculation))
except (ValueError, TypeError) as error:
    print(error)