# Boolean 21 masala

a = int(input(" Uch xonali sonni kiriting = "))

# Sonning raqamlari o'sish tartibida ekanligini  aniqlaymiz
osish_tartibi = a // 100 < a % 100 // 10 and  a % 100 // 10 < a % 10

# True chiqsa o'sish tartibida False o'sish tartibida emas
print(osish_tartibi)