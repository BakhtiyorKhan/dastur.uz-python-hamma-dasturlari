# kutubxona kiiritb olamiz
import math
# A ni kiritib olamiz
a = int(input(" A ni kiriting = "))
# B ni kiritib olamiz
b = int(input(" B ni kiriting = "))
# c ni kiritib olamiz
c = int(input(" C ni kiriting = "))
# Determinatni hisoblab olamiz
d = b ** 2 - 4 * a * c
# x1 hisoblab olamiz
x1 = ( - b + math.sqrt(d)) / ( 2 * a )
# x2 hisoblab olamiz
x2 = ( - b - math.sqrt(d)) / ( 2 * a )
# x1 qiymatini ekranga chiqaramiz
print(" x1 = ",x1)
# x2 qiymatini ekranga chiqaramiz
print(" x2 = ",x2)