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
# Ikki nuqta orasidagi masofani topamiz
ikki_nuqta_masofa = math.sqrt(( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2)
# Ikki nuqta orasidagi masofani ekranga chiqaramiz
print("Ikki nuqta orasidagi masofani = ",ikki_nuqta_masofa)