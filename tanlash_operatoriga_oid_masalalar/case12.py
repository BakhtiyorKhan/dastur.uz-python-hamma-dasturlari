# Case 12 masalasi
import math

print("1-radius, 2-diametr, 3-uzunligi, 4-yuzasi shu qiymatlaridan birini kiriting")
qiymat = int( input(" Qiymatini kiriting = "))
print("--------Doiraning elementlarini tanglang--------")
print("1-radius, 2-diametr, 3-uzunligi, 4-yuzasi")
tanlang = input(" Tanlang = ")

# PI ning constanta qiymati
PI = 3.14

# dasturini tuzamiz
if tanlang == '1':
    diametr = 2 * qiymat
    uzunlik = 2 * PI * qiymat
    yuza = PI * qiymat ** 2
    print(f" Diametr = {diametr}\n Uzunlik = {uzunlik}\n Yuzasi = {yuza}")
elif tanlang == '2':
    radius = qiymat / 2
    uzunlik = PI * qiymat
    yuza = PI * (qiymat/2) ** 2
    print(f" Radius = {radius}\n Uzunlik = {uzunlik}\n Yuzasi = {yuza}")
elif tanlang == '3':
    radius = qiymat / (PI * 2)
    diametr = qiymat / PI
    yuza = PI * radius ** 2
    print(f" Radius = {radius}\n Diametr = {diametr}\n Yuzasi = {yuza}")
elif tanlang == '4':
    radius = math.sqrt(qiymat / PI)
    diametr = 2 * radius
    uzunlik = 2 * PI * radius
    print(f" Radius = {radius}\n Diametr = {diametr}\n Uzunlik = {uzunlik}")
else:
    print(" Xato kiritdizngiz!")


