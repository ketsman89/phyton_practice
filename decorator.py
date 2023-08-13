lst = [1, 2, 3, 4, 5, 6, 7, 8]
d = {"k":3, "l":4}

def check_len(func):
    def wrapper_decorator(*args, **kwargs):
        if len(*args) > 10:
            return "Too many"
        value = func(*args, **kwargs)
        value = value/2
        return value    
    return wrapper_decorator

@check_len
def my_func(lst):
    return(len(lst))

print(my_func(lst))