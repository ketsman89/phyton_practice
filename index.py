a = float(input("Введите свой вес, кг:"))
b = float(input("Введите совй рост, см:"))
c = (a/((b*0.01)**2))
print("Ваш ИМТ:", round(c))
min = 20
max = 50
d = ['=','=','=','=','=','=','=','=','=','=','=','=','=','=','=', ]
i = round((c - 20)/((max - min)/len(d))) - 1
d[i] = "|"
h = ' '.join(d)
print(min, h, max)