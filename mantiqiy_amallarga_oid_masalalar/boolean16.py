# Boolean 16 masala

son = int(input(" Sonni kiriting = "))

# Ikki xonali sonligini aniqlaymiz
ikki_xona = son % 2 == 0 and son % 100 // 10 > 0

# True chiqsa ikki xonali bo'lmasa ikki xonali son emas
print(ikki_xona)