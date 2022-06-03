# For 30 masalasi
import math

n = int(input(" n = "))
print(" a < b haqiqiy sonlar")
a = float(input(" a = "))
b = float(input(" b = "))

qadam = (b-a)/n

for i in range(1,n+1):
    print(f"1-sin({a})={1-math.sin(a)}")
    a += qadam