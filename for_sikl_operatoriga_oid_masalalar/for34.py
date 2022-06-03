# For 34 masalasi

n = int(input(" n = "))

A1 = 1
A2 = 2

for i in range(2,n):
    A = (A2 + 2 * A1)/3
    A1 = A2
    A2 = A

print(" n ta hadi yig'indisi = ",A2)