# For 36 masalasi

n = int(input(" n = "))
k = int(input(" k = "))

sum = 0
# dasturni tuzamiz
for i in range(1,n):
    kopaytma = 1
    for j in range(1,k):
        kopaytma *= i
    sum += kopaytma

print(f" Yig'indi = {sum}")