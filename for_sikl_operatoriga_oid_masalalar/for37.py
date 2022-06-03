# For 37 masalasi

n = int(input(" n = "))

sum = 0
# dasturni tuzamiz
for i in range(1,n):
    kopaytma = 1
    for j in range(1,i):
        kopaytma *= i
    sum += kopaytma

print(f" Yig'indi = {sum}")