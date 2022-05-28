# Boolean 28 masala

x = int(input(" x ning qiymatini kiriting = "))
y = int(input(" y ning qiymatini kiriting = "))

# Birinchi yoki uchinchi choragida yotishini yoki yotmasligini aniqlaymiz
chorak_bir_uch = x > 0 and y > 0 or x < 0 and y < 0

# True chiqsa birinchi yoki uchinchi chorakda False boshqa chorak
print(chorak_bir_uch)