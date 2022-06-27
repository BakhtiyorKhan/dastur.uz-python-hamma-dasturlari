# While 29 masala
import math

e = float(input(" e = "))

# a1 boshlang'ich qiymati
a1 = 1
a2 = 2
i = 1

while 1:
    a = (a1 + 2 * a2) / 3
    i += 1
    if math.fabs(a - a1) < e:
        print(f" {i} \n {a1} \n {a2} {math.fabs(a - a1)}")
        break
    a1 = a2
    a2 = a