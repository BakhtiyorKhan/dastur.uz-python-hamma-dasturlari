# Case 20 masalasi

kun = int(input(" Kunni kiriting = "))
oy = int(input(" Oyni kiriting = "))

# Bu dasturda shart operatorida ishlatganimiz uchun lug'at shart emas ekan

if ( kun > 19 and oy == 1) or ( kun < 19 and oy ==2 ):
    print(" Qovg'a")
elif ( kun > 18 and oy == 2) or ( kun < 21 and oy ==3 ):
    print(" Baliq")
elif ( kun > 20 and oy == 3) or ( kun < 20 and oy ==4 ):
    print(" Qo'y")
elif ( kun > 19 and oy == 4) or ( kun < 21 and oy ==5 ):
    print(" Buzoq")
elif ( kun > 20 and oy == 5) or ( kun < 22 and oy ==6 ):
    print(" Egizaklar")
elif ( kun > 21 and oy == 6) or ( kun < 23 and oy ==7 ):
    print(" Qisqichbaqa")
elif ( kun > 22 and oy == 7) or ( kun < 23 and oy ==8 ):
    print(" Arslon")
elif ( kun > 22 and oy == 8) or ( kun < 23 and oy ==9 ):
    print(" Parizod")
elif ( kun > 22 and oy == 9) or ( kun < 23 and oy ==10 ):
    print(" Tarozi")
elif ( kun > 22 and oy == 10) or ( kun < 23 and oy ==11 ):
    print(" Chayon")
elif ( kun > 22 and oy == 11) or ( kun < 22 and oy ==12 ):
    print(" O'qotar")
elif ( kun > 21 and oy == 12) or ( kun < 20 and oy ==1 ):
    print(" Echki")
else:
    print(" Xato kiritildi")