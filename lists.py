my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list2 = [123, 456, 789]
print(my_list)
my_list.insert(0, "abc")
print(my_list)
my_list.append(my_list2[2])
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.index(789))
removed = my_list.pop(2)
print(my_list)
print(removed)
my_list.remove('abc')
my_list.sort()
print(my_list)
del my_list[2]
print(my_list)
print(len(my_list))
print(max(my_list))
print(sum(my_list))
print(my_list.clear())
lst = ['one', 'two', 'three', 'seven', 'five']
print(lst[4:1:-2])
a_string = 'Я - строка! И я не изменяемый тип данных!'
a_string[0]
a_string = 'о' + a_string[5:]
print(a_string)