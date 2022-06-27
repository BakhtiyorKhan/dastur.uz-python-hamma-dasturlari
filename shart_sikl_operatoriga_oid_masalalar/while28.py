# While 28 masala
import math

e = float(input(" e = "))

# a1 boshlang'ich qiymati
a1 = 2
i = 1

while 1:
    a = 2 + float(1 / a1)
    i +=1
    if math.fabs(a - a1) < e:
        print(f" {i} \n {a1} \n {a}")
        break
    a1 = a
