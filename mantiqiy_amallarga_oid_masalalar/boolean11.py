# Boolean 11 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))

# Sonlarni tekshiramiz A yoki B sonlarni ikkitasi  toq  yoki juft sonligini aniqlaymiz
bir_xilligi =  ( a % 2 == 1 and b % 2 == 1 ) or ( a % 2 == 0 and b % 2 == 0 )

# True bo'lsa ikkitasi ham juft yoki toq sonlar,  False chiqsa bittasi toq yoki juft
print(bir_xilligi)