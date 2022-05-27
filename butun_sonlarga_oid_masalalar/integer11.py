# Integer 11 masalasi

son  = int(input(" Uch xonali son kiriting = "))

# Yuzlik xonasidagi, o'nlik xonasidagi va birlik xonasidagining yig'indisini topamiz
yigindi = son // 100 + son % 100 // 10 + son % 10

print(" Raqamlar yig'indisi = ",yigindi)