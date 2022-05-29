# If 12 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))

# Uchta sondan kichigini aniqlaymiz
if a > b > c or b > a > c:
    print(" Eng kichigi c = ",c)
elif a > c > b or c > a > b:
    print(" Eng kichigi b = ", b)
elif b > c > a or c > b > a:
    print(" Eng kichigi a = ", a)
else:
    print(" Ularning kamida ikkitasi bir-biriga teng")