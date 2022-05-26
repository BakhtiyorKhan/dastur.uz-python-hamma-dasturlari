# math kutubxona qo'shamiz matematik amallar hisoblash uchun
import math
# X1 nuqtani kiritib olamiz
x1 = int(input(" X1 nuqtani kiriting = "))
# y1 nuqtani kiritib olamiz
y1 = int(input(" y1 nuqtani kiriting = "))
# X2 nuqtani kiritib olamiz
x2 = int(input(" X2 nuqtani kiriting = "))
# y2 nuqtani kiritib olamiz
y2 = int(input(" y2 nuqtani kiriting = "))
# X3 nuqtani kiritib olamiz
x3 = int(input(" X2 nuqtani kiriting = "))
# y2 nuqtani kiritib olamiz
y3 = int(input(" y2 nuqtani kiriting = "))
# a kesma masofani topamiz
a = math.sqrt(( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2)
# b kesma masofani topamiz
b = math.sqrt(( x3 - x1 ) ** 2 + ( y3 - y1 ) ** 2)
# c kesma masofani topamiz
c = math.sqrt(( x3 - x2 ) ** 2 + ( y3 - y2 ) ** 2)
# Perimetrining yarmini topamiz
p = ( a + b + c ) / 2
# Hosil bo'lgam uchburchak yuzasini topamiz
S = math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ))
# Uchburchakning ekranga chiqaramiz
print(" Uchbyrchakning yuzasi = ",S)