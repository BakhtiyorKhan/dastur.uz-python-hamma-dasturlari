# While 3 masala

print(" N > K ")
n = int(input(" N = "))
k = int(input(" K = "))

soni = 0

while n >= k:
    n = n - k
    soni +=1

print(f" Butun qismi {soni} ta qoldiq esa {n}")