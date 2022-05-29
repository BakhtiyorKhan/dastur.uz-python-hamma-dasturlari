# If 20 masalasi

# Math kutubxonasi
import math

a = int(input(" A sonni kiriting = "))
b = int(input(" B sonni kiriting = "))
c = int(input(" C sonni kiriting = "))

# Uchta sonlar A nuqtaga eng yaqin nuqtani  aniqlaymiz
if math.fabs(a - b) > math.fabs( a - c):
    print(f" Yaqin nuqta c = {c} va ular orasidagi masofa {math.fabs(a-c)}")
elif math.fabs(a - c) > math.fabs( a - b):
    print(f" Yaqin nuqta b = {b} va ular orasidagi masofa {math.fabs(a-b)}")
else:
    print(f" B va C ning qiymati bir xil A nuqtagacha ikkisidan ham {math.fabs(a-b)} masofada")