# For 24 masalasi

n = int(input(" n ni kiriting = "))
x = float(input(" x ning qiymatini kiriting = "))

sum = 0
ishora = -1
# cos(x) yaqinlashishni hisoblaymiz
for i in range(0,2*n,2):
    factiral = 1
    ishora *= -1
    for j in range(1,i+1):
        factiral *= j
    sum = sum + float(ishora * float(( x ** i) / factiral))

print(f" Yig'indi = {sum}")