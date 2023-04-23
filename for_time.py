import time
import datetime
dn = datetime.datetime.now().time()
str = dn.strftime("%H:%M:%S")
list = str.split(":")
hours, minutes, seconds = list
hour_0 = hours[0]
hour_1 = hours[1]
minute_0 = minutes[0]
minute_1 = minutes[1]
second_0 = seconds[0]
second_1 = seconds[1]
print(hour_1)
zero = """■■■■■■■■
■■    ■■
■■    ■■
■■    ■■
■■    ■■
■■    ■■
■■    ■■
■■■■■■■■"""
print(zero)
one = """      ■■
        ■■
        ■■
        ■■
        ■■
        ■■
        ■■
        ■■"""

ho = " ".join([zero, one])
print(zero, one)