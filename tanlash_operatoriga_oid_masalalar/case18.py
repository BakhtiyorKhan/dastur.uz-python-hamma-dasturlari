# Case 18 masalasi

print(" 100-999 tagacha son kiriting ")
son = int(input(" Kiriting = "))

yuz = str(son // 100)
on = str(son % 100 // 10)
bir = str(son % 10)

yuzlik = {
    '1': "Yuz",
    '2': "Ikki yuz",
    '3': "Uch yuz",
    '4': "To'rt yuz",
    '5': "Besh yuz",
    '6': "Olti yuz",
    '7': "Yetti yuz",
    '8': "Sakkiz yuz",
    '9': "To'qqiz yuz"
}

onlik = {
    '0': "",
    '1': "o'n",
    '2': "yigirma",
    '3': "o'ttiz",
    '4': "qirq",
    '5': "yellik",
    '6': "oltish",
    '7': "yettish",
    '8': "sakson",
    '9': "to'qson"
}
birlik = {
    '0': "",
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

print(f" {yuzlik[yuz]} {onlik[on]} {birlik[bir]}")
