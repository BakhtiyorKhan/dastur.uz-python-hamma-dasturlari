# For 38 masalasi

n = int(input(" n = "))

sum = 0
# dasturni tuzamiz
for i in range(1,n+1):
    kopaytma = 1
    for j in range(n-i+2,1,-1):
        kopaytma *= i
    sum += kopaytma

print(f" Yig'indi = {sum}")