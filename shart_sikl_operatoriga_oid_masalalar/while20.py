# While 20 masala

n = int(input(" n = "))

soni = 0

while n > 0:
    ikki = n % 10
    n = n // 10
    if ikki == 2:
        soni +=1

if soni > 0:
    print(f" Ikki soni bor va  {soni} ta")
else:
    print(" Ikki soni yo'q")