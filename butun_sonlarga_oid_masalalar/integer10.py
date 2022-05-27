# Integer 10 masalasi

son  = int(input(" Uch xonali son kiriting = "))

# O'nlik xonasidagi sonni topamiz
# Ishlashi 456 % 100 = 56 bundan qoldig'ini  oladi 56 // 10 = 5 butunini oladi shu tartibda
onlik = son % 100 // 10

# Birlik xonasidagi sonni topamiz
birlik = son % 10

print(" O'nlik xonasidagi raqam = ",onlik)
print(" Birlik xomasidagi raqam = ",birlik)