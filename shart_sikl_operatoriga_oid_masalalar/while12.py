# While 12 masala

n = int(input(" n = "))

k=0
sum = 0

while sum < n:
    sum +=k
    k += 1

if sum > n:
    sum -= k

k = k - 1

print(" Yig'indi = ",sum)
print(" Kichik butun son = ",k)