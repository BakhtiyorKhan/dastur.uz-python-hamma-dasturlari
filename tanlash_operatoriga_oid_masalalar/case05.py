# Case 5 masalasi

a = float(input(" Sonni kiriting = "))
b = float(input(" Sonni kiriting = "))

amal = input(" Amalni tanglang 1-qo'shish, 2-ayirish, 3-bo'lish va 4-ko'paytirish = ")

# Amal bo'yicha bajaramiz
amal_bajarish = {
    '1': a + b,
    '2': a - b,
    '3': a * b,
    '4': a / b
}

print(f" Qiymat = {amal_bajarish[amal]}")