#rekurs
list_a = [3, 2, 25, [3, 4, 15, [23, 24, [222, 223]],  "gus"], 3, 2, 1]

def list_printer(some_list):
    for el in some_list:
        if isinstance(el, list):
            list_printer(el)
        else:
            print(el)

a = list_printer(list_a)

print(a)
    