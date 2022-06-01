# For 13 masalasi

n = int(input(" n ni kiriting = "))

kopaytma = 0
son = 10
ishora = -1
# Takrorlanishishni bajaramiz
for i in range(1,n+1):
    son += 1
    ishora *= -1
    kopaytma = kopaytma + (ishora * (son/10))

print(kopaytma)
