# def val_checker(test_x):
#     """ Пределать этот CODE!!! """
#     def actuval_decorator(func):
#         def wrapper(x):
#             if test_x(x):
#                 return func(x)
#             else:
#                 raise ValueError(f"wrong val {x}")
#         return wrapper
#     return actuval_decorator

def actual_decorator(func):
    def wrapper(x):
        if func(x) > 0:
            return func(x)
        else:
            print("You rade dude")
    return wrapper

@actual_decorator
def calc_func(x):
    return x ** 3

print(calc_func(6.2))
