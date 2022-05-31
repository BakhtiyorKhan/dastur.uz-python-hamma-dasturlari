# Case 14 masalasi
import math

print("1-tomoni, 2-ichki chizilgan aylananing radiusi, 3-tashqi chizilgan aylananing radiusi, 4-yuzasi shu qiymatlaridan birini kiriting")
qiymat = int( input(" Qiymatini kiriting = "))
print("--------Teng tomonli uchburchak elementlarini tanglang--------")
print("1-tomoni, 2-ichki chizilgan aylananing radiusi, 3-tashqi chizilgan aylananing radiusi, 4-yuzasi")
tanlang = input(" Tanlang = ")

# dasturini tuzamiz
if tanlang == '1':
    ichki_radiusi = qiymat * math.sqrt(3) / 6
    tashqi_radiusi = ichki_radiusi * 2
    yuza = math.sqrt(3) / 4 * qiymat ** 2
    print(f" Ichki radiusi = {ichki_radiusi}\n Tashqi radiusi = {tashqi_radiusi}\n Yuzasi = {yuza}")
elif tanlang == '2':
    tomon = qiymat * 6 /math.sqrt(3)
    tashqi_radiusi = qiymat * 2
    yuza = math.sqrt(3) / 4 * tomon ** 2
    print(f" Tomon = {tomon}\n Tashqi radiusi = {tashqi_radiusi}\n Yuzasi = {yuza}")
elif tanlang == '3':
    ichki_radiusi = qiymat / 2
    tomon = ichki_radiusi * 6 / math.sqrt(3)
    yuza = math.sqrt(3) / 4 * tomon ** 2
    print(f" Tomon = {tomon}\n Ichki radiusi = {ichki_radiusi}\n Yuzasi = {yuza}")
elif tanlang == '4':
    tomon = math.sqrt( 4 * qiymat / math.sqrt(3))
    ichki_radiusi = tomon * math.sqrt(3) / 6
    tashqi_radiusi = ichki_radiusi * 2
    print(f" Tomon = {tomon}\n Ichki radiusi = {ichki_radiusi}\n Tashqi radiusi = {tashqi_radiusi}")
else:
    print(" Xato kiritdizngiz!")


