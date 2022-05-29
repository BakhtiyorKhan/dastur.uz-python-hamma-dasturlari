# If 29 masala

son = int(input(" Sonni kiriting = "))

# Sonni qanday son ekanligini aniqlaymiz
if son > 0 and son % 2 == 0:
    print(" Musbat juft son")
elif son > 0 and son % 2 == 1:
    print(" Musbat toq son")
elif son < 0 and son % 2 == 0:
    print(" Manfiy juft son")
elif son < 0 and son % 2 == 1:
    print(" Manfiy toq son")
else:
    print(" Nolga teng son")