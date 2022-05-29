# If 15 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))

# Uchta sondan ikkitasining yig'indisi katta bo'ladigan  sonlarni topamiz
if a + b > b + c :
    print(f" a = {a} \n b = {b}")
elif a + c > b + c:
    print(f" a = {a} \n c = {c}")
elif b + c > a + c:
    print(f" b = {b} \n c = {c}")
else:
    print(" Ularning kamida ikkitasi bir-biriga teng")