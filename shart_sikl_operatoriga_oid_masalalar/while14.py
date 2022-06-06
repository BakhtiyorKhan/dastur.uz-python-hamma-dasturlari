# While 14 masala

a = int(input(" a = "))

k=0
sum = 0

while sum < a:
    k += 1
    sum += 1/k

if sum > a:
    sum -=1/k
k -=1
print(" Yig'indi = ",sum)
print(" Kichik butun son = ",k)