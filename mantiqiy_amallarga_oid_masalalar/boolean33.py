# Boolean 33 masala

a = int(input(" A tomonni kiriting = "))
b = int(input(" B tomonni kiriting = "))
c = int(input(" C tomonni kiriting = "))

# Uchburchak yasash mumkinmi yoki mumkinmasligini aniqlaymiz
uchburchak = ( a + b ) > c and ( a + c ) > b and ( b + c ) > a

# Uchbuchak yasash mumkin bo'lsa True, bo'lmasa False
print(uchburchak)