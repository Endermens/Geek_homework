def val_checker(test_x):
    """ Пределать этот кринж!!! """
    def actuval_decorator(func):
        def wrapper(x):
            if test_x(x):
                return func(x)
            else:
                raise ValueError(f"wrong val {x}")
        return wrapper
    return actuval_decorator

@val_checker(lambda x: x > 0)
def calc_func(x):
    return x ** 3

print(calc_func(-6.2))
