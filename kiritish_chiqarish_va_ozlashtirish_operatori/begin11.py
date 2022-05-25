# math kutubxona qo'shamiz matematik amallar hisoblash uchun
import math
#  a ni kiritib olyapmiz
a = int(input(" a sonni kiriting = "))
#  b ni kiritib olyapmiz
b = int(input(" b sonni kiriting = "))
# Ikki sonning yig'indisi
yigindi = a + b
# Ikki sonning ko'paytmasi
kopaytma = a * b
# a sonning moduli math kutubxonasidan fabs funksiyasidan foydalanamiz
a_moduli = math.fabs(a)
# b sonning moduli math kutubxonasidan fabs funksiyasidan foydalanamiz
b_moduli = math.fabs(b)
# Ikki sonning yig'indisi natijasini ekranga chiqaramiz
print(" Ikki sonning yig'indisi = ",yigindi)
# Ikki sonning ko'oaytmasi natijasini ekranga chiqaramiz
print(" Ikki sonnig ko'paytmasi = ",kopaytma)
# a sonning moduli natiiasi ekranga chiqaramiz
print(" a sonning moduli = ", a_moduli)
# b sonning moduli natiiasi ekranga chiqaramiz
print(" b sonning moduli = ", b_moduli)