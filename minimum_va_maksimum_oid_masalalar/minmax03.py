# Minmax 3 masalasi

n = int(input(" To'rtburchaklar sonini kiriting = "))

print("1 - to'rtburchak tomonlarini kiriting")
a = int(input(' a = '))
b = int(input(" b = "))

max = 2 * (a + b)

for i in range (1,n):
    if max < 2 * (a + b):
        max = 2 * (a + b)
    print((i+1)," - to'rtburchak tomonlarini kiriting")
    a = int(input(' a = '))
    b = int(input(" b = "))

if max < 2 * (a + b):
    max = 2 * (a + b)

print(f" Eng katta perimetri = {max}")