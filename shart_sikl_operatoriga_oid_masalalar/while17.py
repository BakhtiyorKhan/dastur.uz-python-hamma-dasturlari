# While 17 masala

n = int(input(" n = "))
m = int(input(" m = "))

butun = 0

while n > m :
    n -= m
    butun +=1

print(f" Butuni = {butun} qoldiq = {n}")
