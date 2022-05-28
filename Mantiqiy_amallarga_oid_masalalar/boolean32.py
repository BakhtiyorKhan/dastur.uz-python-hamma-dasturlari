# Boolean 32 masala

a = int(input(" A tomonni kiriting = "))
b = int(input(" B tomonni kiriting = "))
c = int(input(" C tomonni kiriting = "))

# To'g'ri uchburchak ekanligini aniqlaymiz
togri_uchburchak = ( a ** 2 + b ** 2 ) == c ** 2 or ( a ** 2 + c ** 2 ) == b ** 2 or ( c ** 2 + b ** 2 ) == a ** 2

# To'g'ri uchburchak bo'lsa True, bo'lmasa False
print(togri_uchburchak)