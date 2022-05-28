# Boolean 8 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))

# Sonlarni tekshiramiz A va B sonlarni toq sonligini aniqlaymiz
toq_son = a % 2 == 1 and b % 2 == 1

# True bo'lsa toq sonlar yoki False bo'lsa juft sonlar
print(toq_son)