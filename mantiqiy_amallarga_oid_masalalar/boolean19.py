# Boolean 19 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))
c = int(input(" C sonini kiriting = "))

# Sonlarni tekshiramiz hech bo'lmaganda ikkitasi o'zaro qarama-qarshilini  aniqlaymiz
qarama_qarshi = ( a == -b ) or ( a == -c ) or ( b == -c )

# True chiqsa bir jufti qarama-qarshi teng False chiqsa qarama-qarshi son yo'q
print(qarama_qarshi)