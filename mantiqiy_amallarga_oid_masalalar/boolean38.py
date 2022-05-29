# Boolean 38 masala

x1 = int(input(" x1 ni kiriting = "))
y1 = int(input(" y1 ni kiriting = "))
x2 = int(input(" x2 ni kiriting = "))
y2 = int(input(" y2 ni kiriting = "))

# Oq va qora qiymatlarini qo;shib olamiz
qora = x1 + x2
oq = y1 + y2

# Shohing bir yurishda bir maydondan ikkinchisiga o'tishi mumkinligini aniqlaymiz
aniqlash = (    ( oq == qora ) or
                ((qora + 2) == oq) or (qora - 2 ) == oq or
                ((qora + 4) == oq) or (qora - 4 ) == oq or
                ((qora + 6) == oq) or (qora - 6 ) == oq or
                ((qora + 8) == oq) or (qora - 8 ) == oq or
                ((qora + 10) == oq) or (qora - 10 ) == oq or
                ((qora + 12) == oq) or (qora - 12 ) == oq or
                ((qora + 14) == oq) or (qora - 14 ) == oq 
            )


# True chiqsa bir maydon ikkinchisiga o'ta oladi False chiqsa yo'q
print(aniqlash)