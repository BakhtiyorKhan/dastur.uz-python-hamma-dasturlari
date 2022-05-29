# If 13 masalasi

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))

# Uchta sondan o'rtasidagi sonni topamiz
if a > b > c or c > b > a:
    print(" Ularning o'rtasidagi son b = ", b)
elif a > c > b or b > c > a:
    print(" Ularning o'rtasidagi son c = ", c)
elif b > a > c or c > a > b:
    print(" Ularning o'rtasidagi son a = ", a)
else:
    print(" Ularning kamida ikkitasi bir-biriga teng")