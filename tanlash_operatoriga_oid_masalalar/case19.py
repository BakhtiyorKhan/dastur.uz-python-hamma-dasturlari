# Case 19 masalasi
import  math
yil = int(input(" Tug'ilgan yilingizni kiriting = "))

#  Bu formuladan yil qaysi ranga to'g'ri kelishini aniqlaymiz
muchal_rang = str(int(math.fabs((yil - 1984)) // 60 % 5))

# Bu formuladan yil qaysi hayvonga to'g'ri kelishin aniqlaymiz
muchal_hayvon = str(int(math.fabs((yil - 1984) % 12)))

rang = {
    '0': "Yashil",
    '1': "Qizil",
    '2': "Sariq",
    '3': "Oq",
    '4': "Qora"
}

hayvon = {
    '0': "sichqon",
    '1': "sigir",
    '2': "yo'lbars",
    '3': "quyon",
    '4': "ajdar",
    '5': "ilon",
    '6': "ot",
    '7': "qo'y",
    '8': "maymun",
    '9': "tovuq",
    '10': "it",
    '11': "to'ng'iz"
}

print(f" {yil}-yil {rang[muchal_rang]} {hayvon[muchal_hayvon]} yili")


