# For 33 masalasi

n = int(input(" n = "))

F1 = 1
F2 = 1

for i in range(2,n):
    F = F1 + F2
    F1 = F2
    F2 = F

print("Fibonachi soni = ",F2)