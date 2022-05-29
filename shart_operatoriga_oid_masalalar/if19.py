# If 19 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))
d = int(input(" D sonni kiriting = "))

# To'rtta sonlar o'zora uchtasi tengligini aniqlaymiz
if a == b == c and a != d:
    print(f" d = {d} tartib raqami 4")
elif a == b == d and a != c:
    print(f" c = {c} tartib raqami 3")
elif a == c == d and a != b:
    print(f" b = {b} tartib raqami 2")
elif b == c == d and b != a:
    print(f" a = {a} tartib raqami 1")
else:
    print(f" Kiritilgan sonning hammasi bir-biriga teng")