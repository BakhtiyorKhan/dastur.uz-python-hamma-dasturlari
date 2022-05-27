# Integer 12 masalasi

son  = int(input(" Uch xonali son kiriting = "))

# Raqamlarning o'rnini almashtiramiz topamiz
yangi_son = son % 10 * 100 + son % 100 // 10 * 10 + son // 100

print(" Yangi ikki xonali son = ",yangi_son)