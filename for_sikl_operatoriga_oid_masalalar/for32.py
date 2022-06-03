# For 32 masalasi

n = int(input(" n = "))

A0 = 1

for i in range(1,n):
    A1 = (A0 + 1) / i
    A0 = A1

print("Yig'indisi = ",A0)