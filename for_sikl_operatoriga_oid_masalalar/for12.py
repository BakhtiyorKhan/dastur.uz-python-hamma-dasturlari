# For 12 masalasi

n = int(input(" n ni kiriting = "))

kopaytma = 1
son = 10

# Takrorlanishishni bajaramiz
for i in range(1,n+1):
    son += 1
    kopaytma *= (son/10)

print(kopaytma)

