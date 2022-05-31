# Case 16 masalasi

print(" Yoshingizni kiriting 1-69 yoshgacha")
yosh = int(input(" Kiriting = "))

onlik = str(yosh // 10)
birlik = str(yosh % 10)

yosh_onlik = {
    '1': "O'n",
    '2': "Yigirma",
    '3': "O'ttiz",
    '4': "Qirq",
    '5': "Yellik",
    '6': "Oltmish",
    '7': "Yetmish",
    '8': "Sakson",
    '9': "To'qson"
}
yosh_birlik = {
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

print(f" {yosh_onlik[onlik]} {yosh_birlik[birlik]} yoshdasizda")
