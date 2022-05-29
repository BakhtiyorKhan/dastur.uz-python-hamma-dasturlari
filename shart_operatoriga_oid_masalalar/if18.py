# If 18 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))

# Uchta sonlar o'zora ikkitasi tengligini aniqlaymiz
if a == b and a != c:
    print(f" c = {c} tartib raqami 3")
elif a == c and a != b:
    print(f" b = {b} tartib raqami 2")
elif b == c and b != a:
    print(f" a = {a} tartib raqami 1")
else:
    print(f" Kiritilgan sonning hammasi bir-biriga teng")