# If 11 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))

# Shartdan  bir-biriga teng emasligi tekshiramiz
if a != b:
    # Kattasini aniqlaymiz
    if a > b:
        b = a
    else:
        a = b
# Shartlar to'g'ri bo'lmasa nolni o'zlashtiramiz
else:
    a = 0
    b = 0

print(f" a = {a} \n b = {b}")