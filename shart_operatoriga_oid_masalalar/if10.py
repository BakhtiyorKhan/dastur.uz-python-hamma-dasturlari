# If 10 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))

# Shartni tekshiramiz bir-biriga teng bo'lmasa yig'indisi olamiz
if a != b:
    a = a + b
    b = a
# Shartlar to'g'ri bo'lmasa nolni o'zlashtiramiz
else:
    a = 0
    b = 0

print(f" a = {a} \n b = {b}")
