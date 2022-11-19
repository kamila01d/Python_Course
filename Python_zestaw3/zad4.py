import functools

def pamiec(func):
    dict_ = {}
    dict_[0] = 1
    dict_[1] = 1
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[0] in dict_:
            return dict_[args[0]]

        dict_[args[0]] = func(args[0])

        return dict_[args[0]]

    return wrapper

@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(100):
    print(fibonacci(i))
