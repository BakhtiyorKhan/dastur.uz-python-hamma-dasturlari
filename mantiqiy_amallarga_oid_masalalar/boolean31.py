# Boolean 31 masala

a = int(input(" A tomonni kiriting = "))
b = int(input(" B tomonni kiriting = "))
c = int(input(" C tomonni kiriting = "))

# Teng yonli yoki teng yonlimasligini aniqlaymiz
teng_yonli = a == b and a != c or a == c and a != b or b == c and b != a

# Teng yonli bo'lsa True, bo'lmasa False
print(teng_yonli)