# Minmax 1 masalasi

n = int(input(" Sonlar to'plami kiriting = "))

son = int(input(' '))

min = son
max = son

for i in range (1,n):
    if min > son:
        min = son
    if max < son:
        max = son

    son = int(input(' '))

if min > son:
    min = son
if max < son:
    max = son
print(f" Eng kichigi = {min} \n Eng kattasi = {max}")