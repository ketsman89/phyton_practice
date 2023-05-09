# class Dog:
#     def __init__(self):
#         print("hello")

# class Cat:
#     pass

# dog = Dog()
# dog1 = Dog()

# dog.paws = 4
# dog.name = "Snoopy"

# print(dog.name)

# class Dog:
#     def __init__(self, a = "Jack", age = 5):
#         self.name = a
#         self.age = age

# lord = Dog("Lord", 2)
# print(lord.age, lord.name)


class Dog:
    paws = 4 # это свойство класса, а ниже объекта созданного по классу
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, times):
        print(f"{self.name} barks {times} times has age {self.age}")

    def run(self):
        print(f"{self.name} runs")
        self.bark(4)

d = Dog("Graf", 3)
j = Dog("Juchcka", 3)

j.bark(100)