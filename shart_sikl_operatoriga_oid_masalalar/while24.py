# While 24 masala

n = int(input(" n = "))

# sanash uchun ishlatamiz
i = 2
# Fibonachchi bo'shlang'ich qiymati
f1 = 1
f2 = 1

while i < n:
    f = f1 + f2
    f1 = f2
    f2 = f

    i+=1

print(f" {n}-fibonachchi soni qiymati {f2}")