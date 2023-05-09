my_list = [1, 2, 4, [3, 7, 8, [11, 58]], 18, 3]
def list_checker(some_list):
    for el in some_list:
        if isinstance(el, list):
            list_checker(el)
        else:
            print(el)

list_checker(my_list)
