# Case 7 masalasi

kilo = float(input(" Kilogrammni kiriting = "))

print(" Kilogrammni qaysi birlikda kiritgan bo'lsangiz shuni kiriting")
print(" 1-kilogramm, 2-milligramm, 3-gramm, 4-tonna va 5-sentner")
amal = input(" Tanlang = ")

# Shartni tekshiramiz
topish_amal = {
    '1': kilo,
    '2': kilo / 1000 / 1000,
    '3': kilo / 1000,
    '4': kilo * 1000,
    '5': kilo * 100
}

print(f" Kiritilgan qiymati {topish_amal[amal]}  kilogrammga teng")