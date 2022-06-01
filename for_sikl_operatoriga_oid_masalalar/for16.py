# For 16 masalasi

n = int(input(" n ni kiriting = "))
a = int(input(" a ni kiriting = "))

daraja = 1
# darajani hisoblaymiz
for i in range(1,n+1):
    daraja *= a
    print(f" a ning {i} darajasi = {daraja}")
