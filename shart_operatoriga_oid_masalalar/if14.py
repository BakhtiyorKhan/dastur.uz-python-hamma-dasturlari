# If 14 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))

# Uchta sondan avval kattasini keyin kichigini  sonni topamiz
if a > b > c :
    print(f" Kichigi c = {c} \n Kattasi a = {a}")
elif a > c > b :
    print(f" Kichigi b = {b} \n Kattasi a = {a}")
elif b > a > c :
    print(f" Kichigi c = {c} \n Kattasi b = {b}")
elif b > c > a:
    print(f" Kichigi a = {a} \n Kattasi b = {b}")
elif c > a > b :
    print(f" Kichigi b = {b} \n Kattasi c = {c}")
elif c > b > a:
    print(f" Kichigi a = {a} \n Kattasi c = {c}")

else:
    print(" Ularning kamida ikkitasi bir-biriga teng")