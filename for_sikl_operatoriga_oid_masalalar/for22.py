# For 22 masalasi

n = int(input(" n ni kiriting = "))
x = float(input(" x ning qiymatini kiriting = "))

sum = 1

# darajani hisoblaymiz
for i in range(1,n+1):
    factiral = 1
    for j in range(1,i+1):
        factiral *= j
    sum += ( x ** i) / factiral

print(f" Factarial = {sum}")