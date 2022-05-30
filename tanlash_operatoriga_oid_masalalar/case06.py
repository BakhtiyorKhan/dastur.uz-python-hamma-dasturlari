# Case 6 masalasi

uzunlik = float(input(" Uzunlikni kiriting = "))

print(" Uzunlikni qaysi birlikda kiritgan bo'lsangiz shuni kiriting")
print(" 1-desimetr, 2-kilometr, 3-metr, 4-millimetr va 5-santimetr")
amal = input(" Tanlang = ")

# Shartni tekshiramiz
topish_amal = {
    '1': uzunlik * 10 / 100,
    '2': uzunlik * 1000 ,
    '3': uzunlik,
    '4': uzunlik /1000 / 100,
    '5': uzunlik / 100
}

print(f" Kiritilgan qiymati {topish_amal[amal]}  metrga teng")