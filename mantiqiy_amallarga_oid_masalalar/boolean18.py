# Boolean 18 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))
c = int(input(" C sonini kiriting = "))

# Sonlarni tekshiramiz kamida ikitasi bir-biriga tengligini  aniqlaymiz
ikki_teng = a == b or b == c

# True chiqsa kamida ikkitasi teng False chiqsa bir-biriga teng emas
print(ikki_teng)