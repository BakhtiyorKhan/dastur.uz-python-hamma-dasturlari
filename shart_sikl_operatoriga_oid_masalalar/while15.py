# While 15 masala

summa = float(input(" Bankga qo'yilgan boshlang'ich so'mmani kiriting = "))
foiz = float(input("Har oyda necha % ga oshadi = "))

oy = 0
boshlangich = 2 * summa
foiz = foiz / 100

while summa < boshlangich:
    summa += summa * foiz
    oy +=1
    print(f" {oy} - oy {summa}")

print(f" Oy = {oy}")
print(f" Summa = {summa}")