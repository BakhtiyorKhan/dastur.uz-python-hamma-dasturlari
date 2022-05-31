# Case 11 masalasi

print("-----------Yo'nalishlar-----------")
print("s-shimol, j-janub, q-sharq, g-g'arb")
yonalish = input(" Yo'nalishni tnalang = ")
print("-----------Burilishlar-----------")
print("0-harakatni davom ettirish, 1-chapga burilish, 2-o'nga burilish")
burilish = input(" Burilishni tanlang = ")

# Oyni aniqlaymiz
qutb = {
    's': "Shimol",
    'j': "Janub",
    'q': "Sharq",
    'g': "G'arb",
}
kamonda = {
    '0': " o'nga burildi",
    '1': " chapga burildi",
    '2': " 180 gradusga burildi",
}

print(f" {qutb[yonalish]}{kamonda[burilish]}")