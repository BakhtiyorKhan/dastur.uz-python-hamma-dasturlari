# Minmax 2 masalasi

n = int(input(" To'rtburchaklar sonini kiriting = "))

print("1 - to'rtburchak tomonlarini kiriting")
a = int(input(' a = '))
b = int(input(" b = "))

min = a * b

for i in range (1,n):
    if min > (a * b):
        min = a * b
    print((i+1)," - to'rtburchak tomonlarini kiriting")
    a = int(input(' a = '))
    b = int(input(" b = "))

if min > (a * b):
    min = a * b

print(f" Eng kichigi yuza = {min}")