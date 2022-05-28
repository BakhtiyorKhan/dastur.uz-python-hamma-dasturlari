# Boolean 10 masala

a = int(input(" A sonini kiriting = "))
b = int(input(" B sonini kiriting = "))

# Sonlarni tekshiramiz A yoki B sonlarni kamida bittasi  toq sonligini aniqlaymiz
toq_son =  ( a % 2 == 1 and b % 2 != 1 ) or ( a % 2 != 1 and b % 2 == 1)

# True bo'lsa kamida bittasi toq son yoki False bo'lsa juft sonlar
print(toq_son)