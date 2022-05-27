# Integer 13 masalasi

son  = int(input(" Uch xonali son kiriting = "))

# Raqamlarning o'rnini 456 sonni yangi son 546 almashtiramiz topamiz
yangi_son = son % 100 // 10 * 100 + son // 100 * 10 + son % 10

print(" Yangi ikki xonali son = ",yangi_son)