# math kutubxona qo'shamiz matematik amallar hisoblash uchun
import math
#   Aylananing yuzasini  kiritib olyapmiz
aylana_yuzasi = int(input(" Aylananing yuzasini kiriting = "))
# O'zgarmasni kiritamiz
PI = 3.14
# Aylananing radiusini hisoblaymiz
radius = math.sqrt(aylana_yuzasi / PI)
# Aylananing uzunlig hisoblaymiz
aylana_uzunligi = 2 * PI * radius
# Aylananing radiusini ekranga chiqaramiz
print(" Aylananing radiusi = ",radius)
#  Aylananing yuzasini ekranga chiqaramiz
print(" Aylananing uzunligi = ",aylana_uzunligi)
