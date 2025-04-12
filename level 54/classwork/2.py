def apply_to_list(func, values):
    return [func(x) for x in values]

def square(x):
    return x * x