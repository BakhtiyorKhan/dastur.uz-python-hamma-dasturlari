# For 31 masalasi

n = int(input(" n = "))

A0 = 2

for i in range(1,n):
    A1 = 2 + 1 / A0
    A0 = A1

print("Yig'indisi = ",A0)