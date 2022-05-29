# Boolean 35 masala

x1 = int(input(" x1 ni kiriting = "))
y1 = int(input(" y1 ni kiriting = "))
x2 = int(input(" x2 ni kiriting = "))
y2 = int(input(" y2 ni kiriting = "))

# Berilgan maydonlar bir xil rangdaligini
aniqlash = (( x1 + y1 ) % 2 == ( x2 + y2 ) % 2)

# True chiqsa bir xil rangda False chiqadi
print(aniqlash)