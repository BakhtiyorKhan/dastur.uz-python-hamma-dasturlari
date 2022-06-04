# While 5 masala

n = int(input(" n = "))

daraja = 1
soni = 0

while n > daraja:
    daraja *=2
    soni +=1

if n == daraja:
    print(f"{n} soni 2 ning {soni} darajasi ")
else:
    print(" 2 ning darajasi emas")