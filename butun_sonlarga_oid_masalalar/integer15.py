# Integer 15 masalasi

son  = int(input(" Uch xonali son kiriting = "))

# Raqamlarning o'rnini 258 sonni yangi son 528 almashtiramiz topamiz
yangi_son = son % 100 // 10 * 100 + son // 100 * 10 + son % 10

print(" Yangi ikki xonali son = ",yangi_son)