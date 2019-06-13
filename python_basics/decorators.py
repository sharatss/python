def my_decorator(func):
    def func_wrapper(x):
        print("If this is called, then the function is decorated")
        res = func(x)
        print(res)
    return func_wrapper

@my_decorator
def next_number(x):
    return x+1

next_number(1)
