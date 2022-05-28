# Boolean 9 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))

# Sonlarni tekshiramiz A yoki B sonlarni hech bo'lmaganda bittasi  toq sonligini aniqlaymiz
toq_son = a % 2 == 1 or b % 2 == 1

# True bo'lsa kamida bittasi toq son yoki False bo'lsa juft sonlar
print(toq_son)