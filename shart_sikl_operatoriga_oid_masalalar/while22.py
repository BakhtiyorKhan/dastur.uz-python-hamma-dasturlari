# While 22 masala
import math

n = int(input(" n = "))

tub = True
i = 2
ildiz = math.sqrt(n)

while i <= ildiz:
    if n % i == 0:
        tub = False
        break

    i +=1

if tub:
    print(f" Tub son")
else:
    print(" Tub son emas")