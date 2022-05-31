# Case 15 masalasi

print(" Karta qiymatini kiriting (6-14)")
karta_turi = input(" Kiriting = ")
print(" 1-G'isht, 2-Olma, 3-Chillak, 4-Qarg'a")
tur = input(" Kiriting = ")

# Aniqlash boshlaymiz
karta = {
    '6': "Olti",
    '7': "Yetti",
    '8': "Sakkiz",
    '9': "To'qqiz",
    '10': "O'n",
    '11': "Valet",
    '12': "Dama",
    '13': "Qirol",
    '14': "Tuz"
}
karta_guli = {
    '1': "g'isht",
    '2': "olma",
    '3': "chillak",
    '4': "qarg'a"
}

print(f" {karta[karta_turi]} {karta_guli[tur]}")