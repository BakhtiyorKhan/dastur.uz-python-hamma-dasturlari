# For 35 masalasi

n = int(input(" n > 3 katta n = "))

A1 = 1
A2 = 2
A3 = 3


for i in range(3,n):
    A = A3 + A2 - 2 * A1
    A1 = A2
    A2 = A3
    A3 = A

print(" n ta hadi yig'indisi = ",A3)