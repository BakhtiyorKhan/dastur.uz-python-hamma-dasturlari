# For 40 masalasi

a = int(input(" a = "))
b = int(input(" b = "))

k = 0
# dasturni tuzamiz
for i in range(a,b+1):
    k +=1
    for j in range(1,k+1):
        print(i, end= ' ')
    print()