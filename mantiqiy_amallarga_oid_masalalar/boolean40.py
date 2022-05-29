# Boolean 40 masala

x1 = int(input(" x1 ni kiriting = "))
y1 = int(input(" y1 ni kiriting = "))
x2 = int(input(" x2 ni kiriting = "))
y2 = int(input(" y2 ni kiriting = "))

# Otning bir yurishda bir maydondan ikkinchisiga o'tishi mumkinligini aniqlaymiz
aniqlash = (
            ( x1 + 1 == x2 ) and ( y1 + 2 == y2 or y1 - 2 == y2 ) or
            ( x1 + 2 == x2 ) and ( y1 + 1 == y2 or y1 - 1 == y2 ) or
            ( x1 - 1 == x2 ) and ( y1 + 2 == y2 or y1 - 2 == y2 ) or
            ( x1 - 2 == x2 ) and ( y1 + 1 == y2 or y1 - 1 == y2 )
             )


# True chiqsa bir maydon ikkinchisiga o'ta oladi False chiqsa yo'q
print(aniqlash)