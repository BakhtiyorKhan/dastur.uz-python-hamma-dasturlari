# Case 9 masalasi

kun = input(" Kunni kiriting = ")
oy = input(" Oyni kiriting = ")

# Oyni aniqlaymiz
oy_lug = {
    '1': "Yanvar",
    '2': "Fevral",
    '3': "Mart",
    '4': "Aprel",
    '5': "May",
    '6': "Iyun",
    '7': "Iyul",
    '8': "Avgust",
    '9': "Sentabr",
    '10': "Oktabr",
    '11': "Noyabr",
    '12': "Dekabr",
}

print(f" {int(kun)+1}-{oy_lug[oy]}")