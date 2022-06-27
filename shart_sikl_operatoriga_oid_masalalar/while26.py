# While 26 masala

n = int(input(" n = "))

# Fibonachchi bo'shlang'ich qiymati
f1 = 1
f2 = 1
f = 1

while f < n:
    f = f1 + f2
    f1 = f2
    f2 = f

print(f" {f1} \n {f}")