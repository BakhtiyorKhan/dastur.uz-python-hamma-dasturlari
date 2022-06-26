# While 21 masala

n = int(input(" n = "))

soni = 0

while n > 0:
    toq = n % 10
    n = n // 10
    if toq % 2 == 1:
        soni += 1

if soni > 0:
    print(f" Toq sonlar bor va  {soni} ta")
else:
    print(" Toq sonlar yo'q")