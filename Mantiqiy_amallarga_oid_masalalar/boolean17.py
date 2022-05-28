# Boolean 17 masala

son = int(input(" Sonni kiriting = "))

# Uch xonali sonligini aniqlaymiz
uch_xona = son % 2 == 0 and son % 1000 // 100 > 0

# True chiqsa uch xonali bo'lmasa uch xonali son emas
print(uch_xona)