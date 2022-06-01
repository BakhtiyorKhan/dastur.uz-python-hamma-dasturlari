# For 17 masalasi

n = int(input(" n ni kiriting = "))
a = int(input(" a ni kiriting = "))

sum = 0
# darajani hisoblaymiz
for i in range(0,n+1):
    sum += a ** i

print(f" Yig'indi = {sum}")