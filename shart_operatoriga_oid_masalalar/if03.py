# If 3 masalasi

son = int(input(" Sonni kiriting = "))

# Musbat yoki musbatmasligini aniqlaymiz shart bilan
if son > 0 :
    # Musbat bo'lsa birga oshadi
    son += 1
    print(son)
elif son < 0 :
    # Musbat bo'lmasa o'zgarmasdan chiqadi
    print(son)
else:
    # Nolga teng bo'lgani uchun son o'n o'zlashtiradi
    son = 10
    print(son)