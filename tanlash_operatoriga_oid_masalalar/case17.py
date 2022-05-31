# Case 17 masalasi

print(" Nechta masala ekanligini kiriting 1-40 ")
soni = int(input(" Kiriting = "))

onlik = str(soni // 10)
birlik = str(soni % 10)

masala_onlik = {
    '1': "O'n",
    '2': "Yigirma",
    '3': "O'ttiz",
    '4': "Qirq",
}
masala_birlik = {
    '1': "bir",
    '2': "ikki",
    '3': "uch",
    '4': "to'rt",
    '5': "besh",
    '6': "olti",
    '7': "yetti",
    '8': "sakkiz",
    '9': "to'qqiz"
}

print(f" {masala_onlik[onlik]} {masala_birlik[birlik]}ta masala")
