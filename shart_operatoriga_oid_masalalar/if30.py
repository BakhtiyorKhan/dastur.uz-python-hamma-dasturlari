# If 30 masala

son = int(input(" 1-999 bo'lgan son kiriting = "))

# Sonni nechi xonaligini va juft va toqligini aniqlaymiz
if son // 1000 > 0 or son <= 0:
    print(" Siz 999 dan katta son yoki noldan kichik son kiritdingiz")
elif son // 100 > 0 :
    if son % 2 == 0:
        print(" Uch xonali juft son")
    else:
        print(" Uch xonali toq son")
elif son // 10 > 0 :
    if son % 2 == 0:
        print(" Ikki xonali juft son")
    else:
        print(" Ikki xonali toq son")
elif son % 10 > 0 :
    if son % 2 == 0:
        print(" Bir xonali juft son")
    else:
        print(" Bir xonali toq son")
