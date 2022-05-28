# Boolean 29 masala

x = int(input(" x ning qiymatini kiriting = "))
y = int(input(" y ning qiymatini kiriting = "))
x1 = int(input(" x1 ning qiymatini kiriting = "))
y1 = int(input(" y1 ning qiymatini kiriting = "))
x2 = int(input(" x2 ning qiymatini kiriting = "))
y2 = int(input(" y2 ning qiymatini kiriting = "))

# X va Y nuqtalar (X1, Y1) va (X2, Y2) nuqtalarda yotishini yoki yotmasligini aniqlaymiz
x_y_yotishi = x2 < x < x1 and y2 < y <y1

#  X va Y nuqtalar (X1, Y1) va (X2, Y2) nuqtalarda yotsa True, yotmasa False
print(x_y_yotishi)