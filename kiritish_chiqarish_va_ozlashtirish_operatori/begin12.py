# math kutubxona qo'shamiz matematik amallar hisoblash uchun
import math
#  a ni kiritib olyapmiz
a = int(input(" Uchburchakning a katetini kiriting = "))
#  b ni kiritib olyapmiz
b = int(input(" Uchburchakning b katetini kiriting = "))
# c gipotenuzasini hisoblaymiz pifagor formulasi bilan
c = math.sqrt( a ** 2 + b ** 2 )
# Uchbuchak perimetri hisoblaymiz
perimetri = a + b + c
# Uchburchakning perimetrini ekranga chiqaramiz
print(" Uchburchak perimetri = ",perimetri)