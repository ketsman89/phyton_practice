import time
import datetime
import os

while True:
    dn = datetime.datetime.now().time()
    str = dn.strftime("%H:%M:%S")
    list = str.split(":")
    hours, minutes, seconds = list
    hour_0 = int(hours[0])
    hour_1 = int(hours[1])
    minute_0 = int(minutes[0])
    minute_1 = int(minutes[1])
    second_0 = int(seconds[0])
    second_1 = int(seconds[1])

    
    if hour_0 == 0:
        h01 = "■■■■■■■■"
        h02 = "■■    ■■"
        h03 = "■■    ■■"
        h04 = "■■    ■■"
        h05 = "■■    ■■"
        h06 = "■■    ■■"
        h07 = "■■■■■■■■"


    if hour_0 == 1:
        h01 = "      ■■"
        h02 = "      ■■"
        h03 = "      ■■"
        h04 = "      ■■"
        h05 = "      ■■"
        h06 = "      ■■"
        h07 = "      ■■"


    if hour_0 == 2:
        h01 = "■■■■■■■■"
        h02 = "      ■■"
        h03 = "      ■■"
        h04 = "■■■■■■■■"
        h05 = "■■      "
        h06 = "■■      "
        h07 = "■■■■■■■■"

    if hour_1 == 0:
        h11 = "■■■■■■■■"
        h12 = "■■    ■■"
        h13 = "■■    ■■"
        h14 = "■■    ■■"
        h15 = "■■    ■■"
        h16 = "■■    ■■"
        h17 = "■■■■■■■■"


    if hour_1 == 1:
        h11 = "      ■■"
        h12 = "      ■■"
        h13 = "      ■■"
        h14 = "      ■■"
        h15 = "      ■■"
        h16 = "      ■■"
        h17 = "      ■■"


    if hour_1 == 2:
        h11 = "■■■■■■■■"
        h12 = "      ■■"
        h13 = "      ■■"
        h14 = "■■■■■■■■"
        h15 = "■■      "
        h16 = "■■      "
        h17 = "■■■■■■■■"

    if hour_1 == 3:
        h11 = "■■■■■■■■"
        h12 = "      ■■"
        h13 = "      ■■"
        h14 = "■■■■■■■■"
        h15 = "      ■■"
        h16 = "      ■■"
        h17 = "■■■■■■■■"

    if hour_1 == 4:
        h11 = "■■    ■■"
        h12 = "■■    ■■"
        h13 = "■■    ■■"
        h14 = "■■■■■■■■"
        h15 = "      ■■"
        h16 = "      ■■"
        h17 = "      ■■"

    if hour_1 == 5:
        h11 = "■■■■■■■■"
        h12 = "■■      "
        h13 = "■■      "
        h14 = "■■■■■■■■"
        h15 = "      ■■"
        h16 = "      ■■"
        h17 = "■■■■■■■■"


    if hour_1 == 6:
        h11 = "■■■■■■■■"
        h12 = "■■      "
        h13 = "■■      "
        h14 = "■■■■■■■■"
        h15 = "■■    ■■"
        h16 = "■■    ■■"
        h17 = "■■■■■■■■"

    if hour_1 == 7:
        h11 = "■■■■■■■■"
        h12 = "      ■■"
        h13 = "      ■■"
        h14 = "      ■■"
        h15 = "      ■■"
        h16 = "      ■■"
        h17 = "      ■■"


    if hour_1 == 8:
        h11 = "■■■■■■■■"
        h12 = "■■    ■■"
        h13 = "■■    ■■"
        h14 = "■■■■■■■■"
        h15 = "■■    ■■"
        h16 = "■■    ■■"
        h17 = "■■■■■■■■"

    if hour_1 == 9:
        h11 = "■■■■■■■■"
        h12 = "■■    ■■"
        h13 = "■■    ■■"
        h14 = "■■■■■■■■"
        h15 = "      ■■"
        h16 = "      ■■"
        h17 = "■■■■■■■■"

    if minute_0 == 0:
        m01 = "■■■■■■■■"
        m02 = "■■    ■■"
        m03 = "■■    ■■"
        m04 = "■■    ■■"
        m05 = "■■    ■■"
        m06 = "■■    ■■"
        m07 = "■■■■■■■■"


    if minute_0 == 1:
        m01 = "      ■■"
        m02 = "      ■■"
        m03 = "      ■■"
        m04 = "      ■■"
        m05 = "      ■■"
        m06 = "      ■■"
        m07 = "      ■■"


    if minute_0 == 2:
        m01 = "■■■■■■■■"
        m02 = "      ■■"
        m03 = "      ■■"
        m04 = "■■■■■■■■"
        m05 = "■■      "
        m06 = "■■      "
        m07 = "■■■■■■■■"

    if minute_0 == 3:
        m01 = "■■■■■■■■"
        m02 = "      ■■"
        m03 = "      ■■"
        m04 = "■■■■■■■■"
        m05 = "      ■■"
        m06 = "      ■■"
        m07 = "■■■■■■■■"

    if minute_0 == 4:
        m01 = "■■    ■■"
        m02 = "■■    ■■"
        m03 = "■■    ■■"
        m04 = "■■■■■■■■"
        m05 = "      ■■"
        m06 = "      ■■"
        m07 = "      ■■"

    if minute_0 == 5:
        m01 = "■■■■■■■■"
        m02 = "■■      "
        m03 = "■■      "
        m04 = "■■■■■■■■"
        m05 = "      ■■"
        m06 = "      ■■"
        m07 = "■■■■■■■■"


    if minute_1 == 0:
        m11 = "■■■■■■■■"
        m12 = "■■    ■■"
        m13 = "■■    ■■"
        m14 = "■■    ■■"
        m15 = "■■    ■■"
        m16 = "■■    ■■"
        m17 = "■■■■■■■■"


    if minute_1 == 1:
        m11 = "      ■■"
        m12 = "      ■■"
        m13 = "      ■■"
        m14 = "      ■■"
        m15 = "      ■■"
        m16 = "      ■■"
        m17 = "      ■■"


    if minute_1 == 2:
        m11 = "■■■■■■■■"
        m12 = "      ■■"
        m13 = "      ■■"
        m14 = "■■■■■■■■"
        m15 = "■■      "
        m16 = "■■      "
        m17 = "■■■■■■■■"

    if minute_1 == 3:
        m11 = "■■■■■■■■"
        m12 = "      ■■"
        m13 = "      ■■"
        m14 = "■■■■■■■■"
        m15 = "      ■■"
        m16 = "      ■■"
        m17 = "■■■■■■■■"

    if minute_1 == 4:
        m11 = "■■    ■■"
        m12 = "■■    ■■"
        m13 = "■■    ■■"
        m14 = "■■■■■■■■"
        m15 = "      ■■"
        m16 = "      ■■"
        m17 = "      ■■"

    if minute_1 == 5:
        m11 = "■■■■■■■■"
        m12 = "■■      "
        m13 = "■■      "
        m14 = "■■■■■■■■"
        m15 = "      ■■"
        m16 = "      ■■"
        m17 = "■■■■■■■■"

    if minute_1 == 6:
        m11 = "■■■■■■■■"
        m12 = "■■      "
        m13 = "■■      "
        m14 = "■■■■■■■■"
        m15 = "■■    ■■"
        m16 = "■■    ■■"
        m17 = "■■■■■■■■"

    if minute_1 == 7:
        m11 = "■■■■■■■■"
        m12 = "      ■■"
        m13 = "      ■■"
        m14 = "      ■■"
        m15 = "      ■■"
        m16 = "      ■■"
        m17 = "      ■■"


    if minute_1 == 8:
        m11 = "■■■■■■■■"
        m12 = "■■    ■■"
        m13 = "■■    ■■"
        m14 = "■■■■■■■■"
        m15 = "■■    ■■"
        m16 = "■■    ■■"
        m17 = "■■■■■■■■"

    if minute_1 == 9:
        m11 = "■■■■■■■■"
        m12 = "■■    ■■"
        m13 = "■■    ■■"
        m14 = "■■■■■■■■"
        m15 = "      ■■"
        m16 = "      ■■"
        m17 = "■■■■■■■■"

    if second_0 == 0:
        s01 = "■■■■■■■■"
        s02 = "■■    ■■"
        s03 = "■■    ■■"
        s04 = "■■    ■■"
        s05 = "■■    ■■"
        s06 = "■■    ■■"
        s07 = "■■■■■■■■"


    if second_0 == 1:
        s01 = "      ■■"
        s02 = "      ■■"
        s03 = "      ■■"
        s04 = "      ■■"
        s05 = "      ■■"
        s06 = "      ■■"
        s07 = "      ■■"


    if second_0 == 2:
        s01 = "■■■■■■■■"
        s02 = "      ■■"
        s03 = "      ■■"
        s04 = "■■■■■■■■"
        s05 = "■■      "
        s06 = "■■      "
        s07 = "■■■■■■■■"

    if second_0 == 3:
        s01 = "■■■■■■■■"
        s02 = "      ■■"
        s03 = "      ■■"
        s04 = "■■■■■■■■"
        s05 = "      ■■"
        s06 = "      ■■"
        s07 = "■■■■■■■■"

    if second_0 == 4:
        s01 = "■■    ■■"
        s02 = "■■    ■■"
        s03 = "■■    ■■"
        s04 = "■■■■■■■■"
        s05 = "      ■■"
        s06 = "      ■■"
        s07 = "      ■■"

    if second_0 == 5:
        s01 = "■■■■■■■■"
        s02 = "■■      "
        s03 = "■■      "
        s04 = "■■■■■■■■"
        s05 = "      ■■"
        s06 = "      ■■"
        s07 = "■■■■■■■■"


    if second_1 == 0:
        s11 = "■■■■■■■■"
        s12 = "■■    ■■"
        s13 = "■■    ■■"
        s14 = "■■    ■■"
        s15 = "■■    ■■"
        s16 = "■■    ■■"
        s17 = "■■■■■■■■"


    if second_1 == 1:
        s11 = "      ■■"
        s12 = "      ■■"
        s13 = "      ■■"
        s14 = "      ■■"
        s15 = "      ■■"
        s16 = "      ■■"
        s17 = "      ■■"


    if second_1 == 2:
        s11 = "■■■■■■■■"
        s12 = "      ■■"
        s13 = "      ■■"
        s14 = "■■■■■■■■"
        s15 = "■■      "
        s16 = "■■      "
        s17 = "■■■■■■■■"

    if second_1 == 3:
        s11 = "■■■■■■■■"
        s12 = "      ■■"
        s13 = "      ■■"
        s14 = "■■■■■■■■"
        s15 = "      ■■"
        s16 = "      ■■"
        s17 = "■■■■■■■■"

    if second_1 == 4:
        s11 = "■■    ■■"
        s12 = "■■    ■■"
        s13 = "■■    ■■"
        s14 = "■■■■■■■■"
        s15 = "      ■■"
        s16 = "      ■■"
        s17 = "      ■■"

    if second_1 == 5:
        s11 = "■■■■■■■■"
        s12 = "■■      "
        s13 = "■■      "
        s14 = "■■■■■■■■"
        s15 = "      ■■"
        s16 = "      ■■"
        s17 = "■■■■■■■■"

    if second_1 == 6:
        s11 = "■■■■■■■■"
        s12 = "■■      "
        s13 = "■■      "
        s14 = "■■■■■■■■"
        s15 = "■■    ■■"
        s16 = "■■    ■■"
        s17 = "■■■■■■■■"

    if second_1 == 7:
        s11 = "■■■■■■■■"
        s12 = "      ■■"
        s13 = "      ■■"
        s14 = "      ■■"
        s15 = "      ■■"
        s16 = "      ■■"
        s17 = "      ■■"


    if second_1 == 8:
        s11 = "■■■■■■■■"
        s12 = "■■    ■■"
        s13 = "■■    ■■"
        s14 = "■■■■■■■■"
        s15 = "■■    ■■"
        s16 = "■■    ■■"
        s17 = "■■■■■■■■"

    if second_1 == 9:
        s11 = "■■■■■■■■"
        s12 = "■■    ■■"
        s13 = "■■    ■■"
        s14 = "■■■■■■■■"
        s15 = "      ■■"
        s16 = "      ■■"
        s17 = "■■■■■■■■"

    if second_1 % 2 == 0:
        a = "■■"
    else:
        a = "  "






    print(h01 + "  " + h11 + "      " + m01 + "  " + m11 + "      " + s01 + "  " + s11)
    print(h02 + "  " + h12 + "      " + m02 + "  " + m12 + "      " + s02 + "  " + s12)
    print(h03 + "  " + h13 + "  " + a + "  " + m03 + "  " + m13 + "  " + a + "  " + s03 + "  " + s13)
    print(h04 + "  " + h14 + "      " + m04 + "  " + m14 + "      " + s04 + "  " + s14)
    print(h05 + "  " + h15 + "  " + a + "  " + m05 + "  " + m15 + "  " + a + "  " + s05 + "  " + s15)
    print(h06 + "  " + h16 + "      " + m06 + "  " + m16 + "      " + s06 + "  " + s16)
    print(h07 + "  " + h17 + "      " + m07 + "  " + m17 + "      " + s07 + "  " + s17)

    time.sleep(0.3)
    os.system('cls')
