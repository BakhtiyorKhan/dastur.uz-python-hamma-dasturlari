# If 28 masalasi

yil = int(input(" Yilni kiriting = "))

# Kasiba yili yoki yili emasligini aniqlaymiz
if yil % 400 == 0 or ( yil % 100 != 0 and yil % 4 == 0):
    print(" Kasiba yili")
else:
    print(" Kasiba yili emas")