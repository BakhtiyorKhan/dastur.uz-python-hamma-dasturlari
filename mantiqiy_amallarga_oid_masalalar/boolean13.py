# Boolean 13 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))
c = int(input(" C sonini kiriting = "))

# Sonlarni tekshiramiz A, B va C sonlar hech bo'lmaganda bittasi musbat sonligini aniqlaymiz
bitta_musbat =  a > 0 or b > 0 or c > 0

# True chiqsa kamida bittasi musbat False chiqsa hammasi manfiy yoki 0 ga teng
print(bitta_musbat)