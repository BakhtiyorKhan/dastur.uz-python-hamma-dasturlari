# Integer 16 masalasi

son  = int(input(" Uch xonali son kiriting = "))

# Raqamlarning o'rnini 147 sonni yangi son 174 almashtiramiz topamiz
yangi_son = son // 100 * 100 + son % 10 * 10 + son % 100 // 10

print(" Yangi ikki xonali son = ",yangi_son)