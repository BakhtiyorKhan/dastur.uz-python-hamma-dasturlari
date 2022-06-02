# For 25 masalasi

n = int(input(" n ni kiriting = "))
x = float(input(" x ning qiymatini kiriting = "))

sum = 0
ishora = -1
# Yig'indini hisoblaymiz
for i in range(1,n):
    ishora *= -1
    sum = sum + ishora * (x ** i) / i

print(f" Yig'indi = {sum}")