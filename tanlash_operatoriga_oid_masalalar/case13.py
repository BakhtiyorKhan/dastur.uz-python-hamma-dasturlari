# Case 13 masalasi
import math

print("1-katet, 2-gipotenuza, 3-gipotuenuzaga tushirilgan baland, 4-yuzasi shu qiymatlaridan birini kiriting")
qiymat = int( input(" Qiymatini kiriting = "))
print("--------Teng yonli uchburchak elementlarini tanglang--------")
print("1-katet, 2-gipotenuza, 3-gipotuenuzaga tushirilgan baland, 4-yuzasi")
tanlang = input(" Tanlang = ")

# dasturini tuzamiz
if tanlang == '1':
    gipotenuza = qiymat * math.sqrt(2)
    balandlik = gipotenuza / 2
    yuza = gipotenuza * balandlik / 2
    print(f" Gipotenuza = {gipotenuza}\n Balandlik = {balandlik}\n Yuzasi = {yuza}")
elif tanlang == '2':
    katet = qiymat / math.sqrt(2)
    balandlik = qiymat / 2
    yuza = qiymat * balandlik / 2
    print(f" Katet = {katet}\n Balandlik = {balandlik}\n Yuzasi = {yuza}")
elif tanlang == '3':
    gipotenuza = qiymat * 2
    katet = gipotenuza / math.sqrt(2)
    yuza = qiymat * gipotenuza / 2
    print(f" Katet = {katet}\n Gipotenuza = {gipotenuza}\n Yuzasi = {yuza}")
elif tanlang == '4':
    balandlik = math.sqrt(qiymat)
    gipotenuza = balandlik * 2
    katet = gipotenuza / math.sqrt(2)
    print(f" Katet = {katet}\n Gipotenuza = {gipotenuza}\n Balandlik = {balandlik}")
else:
    print(" Xato kiritdizngiz!")


