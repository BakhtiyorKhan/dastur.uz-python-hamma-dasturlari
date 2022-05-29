# Boolean 39 masala

x1 = int(input(" x1 ni kiriting = "))
y1 = int(input(" y1 ni kiriting = "))
x2 = int(input(" x2 ni kiriting = "))
y2 = int(input(" y2 ni kiriting = "))

# Oq va qora qiymatlarini qo;shib olamiz
qora = x1 + x2
oq = y1 + y2

# Farzinning bir yurishda bir maydondan ikkinchisiga o'tishi mumkinligini aniqlaymiz
aniqlash = (    # Filga o'xshab yurish holadi
    
                ( oq == qora ) or
                ((qora + 2) == oq) or (qora - 2 ) == oq or
                ((qora + 4) == oq) or (qora - 4 ) == oq or
                ((qora + 6) == oq) or (qora - 6 ) == oq or
                ((qora + 8) == oq) or (qora - 8 ) == oq or
                ((qora + 10) == oq) or (qora - 10 ) == oq or
                ((qora + 12) == oq) or (qora - 12 ) == oq or
                ((qora + 14) == oq) or (qora - 14 ) == oq or

                #     Shohga o'xshab yurish holati

                ( (x1 == x2 - 1) and (y1 == y2)) or
                ( (x1 == x2 - 1) and (y1 == y2 - 1)) or
                ( (x1 == x2 - 1) and (y1 == y2 + 1)) or
                ( (x1 == x2) and (y1 == y2 + 1)) or
                ( (x1 == x2) and (y1 == y2 - 1)) or
                ( (x1 == x2 + 1) and (y1 == y2)) or
                ( (x1 == x2 + 1) and (y1 == y2 - 1)) or
                ( (x1 == x2 + 1) and (y1 == y2 + 1))
            )


# True chiqsa bir maydon ikkinchisiga o'ta oladi False chiqsa yo'q
print(aniqlash)