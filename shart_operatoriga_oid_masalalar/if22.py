# If 22 masalasi

x = int(input(" x nuqtani kiriting = "))
y = int(input(" y nuqtani kiriting = "))

# Qaysi chorakda yotishini aniqlaymiz
if x > 0 and y > 0:
    print(" Birinchi chorakda")
elif x < 0 and y > 0:
    print(" Ikkinchi chorakda")
elif x < 0 and y < 0:
    print(" Uchinchi chorakda")
elif x > 0 and y < 0:
    print(" To'rtinchi chorakda")
else:
    print(" Ular koordinata boshida yotadi")