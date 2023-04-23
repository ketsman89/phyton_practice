import time
import datetime
import os


# print(str)
# print(type(str))

while True:
    dn = datetime.datetime.now().time()
    str = dn.strftime("%H:%M:%S")
    print(str)
    time.sleep(0.4)    
    os.system('cls')
