# Boolean 27 masala

x = int(input(" x ning qiymatini kiriting = "))
y = int(input(" y ning qiymatini kiriting = "))

# Ikkinchi yoki uchinchi choragida yotishini yoki yotmasligini aniqlaymiz
chorak_ikki_uch = x < 0 and y > 0 or x < 0 and y < 0

# True chiqsa ikkinchi yoki uchinchi chorakda False boshqa chorak
print(chorak_ikki_uch)