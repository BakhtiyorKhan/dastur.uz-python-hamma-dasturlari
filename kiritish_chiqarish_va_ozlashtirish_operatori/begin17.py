# math kutubxona qo'shamiz matematik amallar hisoblash uchun
import math
#  a nuqtani kiritib olyapmiz
a = int(input(" a nuqtani kiriting = "))
#  b nuqtani kiritib olyapmiz
b = int(input(" b nuqtani kiriting = "))
#  c nuqtani kiritib olyapmiz
c = int(input(" c nuqtani kiriting = "))
# AC kesmani uzunligi aniqlaymiz
ac = math.fabs( c - a )
# BC kesmani uzunlig aniqlaymiz
bc = math.fabs( c - b )
# AC va BC kesmalari uzunligi yig'indisi
ac_bc_yigindisi = ac + bc
# AC kesma uzunligini ekranga chiqaramiz
print(" AC kesma uzunligi = ",ac)
# BC kesma uzunligini ekranga chiqaramiz
print(" BC kesma uzunligi = ",bc)
# AC va BC kesma yig'indisini ekranga chiqaramiz
print(" AC va BC kesma yig'indisi = ",ac_bc_yigindisi)