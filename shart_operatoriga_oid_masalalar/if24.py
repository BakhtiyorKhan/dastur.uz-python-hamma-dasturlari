# If 24 masalasi

import math

x = float(input(" x nuqtani kiriting = "))

# Funksiyani sharti bo'yicha tekshiramiz
if x > 0:
    funksiya = 2 * math.sin(x)
    print(" Birinchi shart bajarildi qiymati = ",funksiya)
else:
    funksiya = x - 6
    print(" Ikkinchi shart bajarildi qiymati = ", funksiya)


