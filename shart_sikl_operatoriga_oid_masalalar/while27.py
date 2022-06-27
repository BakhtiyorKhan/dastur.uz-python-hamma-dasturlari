# While 27 masala

n = int(input(" n = "))

# Fibonachchi bo'shlang'ich qiymati
f1 = 1
f2 = 1
f = f1 + f2
i = 1

while f < n:
    f = f1 + f2
    f1 = f2
    f2 = f
    i +=1

print(f" {i} hadi")