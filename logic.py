a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = a > 0 and b > 0 and c > 0
print(d == False or "нет нулей")

f = a > 0 or b > 0 or c > 0
print(f == True or "Введены все нули")
print(a == 0 or a)

if a > b + c:
    print("a - b - c")
if a < b + c:
    print("b + c - a")
if a > 50 and (b > a or c > a ):
    print("Вася")
if a > 5 or a == b == 7:
    print("Петя")
