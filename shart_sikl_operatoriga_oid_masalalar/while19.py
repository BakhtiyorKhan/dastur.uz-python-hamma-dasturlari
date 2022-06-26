# While 19 masala

n = int(input(" n = "))

sum = 0
soni = 0

while n > 0:
    sum += n % 10
    n = n // 10
    soni +=1

print(f" Sonning yig'indisi = {sum} soni = {soni} ta")
