# If 9 masalasi

a = float(input(" A sonni kiriting = "))
b = float(input(" B sonni kiriting = "))

# A son katta bo'lsa b ga qiymati bilan almashtiriladi
if a > b :
    k = a
    a = b
    b = k

print(f" a = {a} \n b = {b}")
