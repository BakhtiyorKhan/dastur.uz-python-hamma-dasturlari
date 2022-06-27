# While 30 masalasi

a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))

k = 2

while a > c and b > c:
    a -= c
    b -= c
    k += 1

k *= 3
print(" k = ",k)