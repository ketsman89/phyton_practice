name = "Andrey"
date = "08.03.2023"
print(f"Hello {name}! Pls visit our store! {date}")
print(True and False)
#user_input = input("type something")
#a = user_input or "u must type something"
#print(a)
a = {1:'sss', 2:'ss'}
print(a.get(1, "такого значения нет"))
print(a.get(3, "такого значения нет"))
string = "aabcdef"
for i in string:
    print(i)
print("The End")
for _ in range(10):
    print("Hello")     
d = {1:"123", 2:"234", 4:"345"}
for key in d:
    print(key, d[key])
our_list = ["kotik", "sobacha", "kutska"]
a = (our_list.__iter__())
print(a.__next__())
from time import sleep
while True:
    inp = input("enter command")
    if inp == 'q':
        break
    else:
        print(inp.upper())

