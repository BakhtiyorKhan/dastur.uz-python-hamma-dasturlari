# If 26 masalasi

x = float(input(" x nuqtani kiriting = "))

# Funksiyani sharti bo'yicha tekshiramiz
if x <= 0:
    funksiya = -x
    print(" Birinchi shart bajarildi qiymati = ",funksiya)
elif 0 < x < 2 :
    funksiya = x ** 2
    print(" Ikkinchi shart bajarildi qiymati = ", funksiya)
else:
    funksiya = 4
    print(" Uchinchi shart bajarildi qiymati = ",funksiya)
