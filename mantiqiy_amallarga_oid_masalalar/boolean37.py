# Boolean 37 masala

x1 = int(input(" x1 ni kiriting = "))
y1 = int(input(" y1 ni kiriting = "))
x2 = int(input(" x2 ni kiriting = "))
y2 = int(input(" y2 ni kiriting = "))

# Shohing bir yurishda bir maydondan ikkinchisiga o'tishi mumkinligini aniqlaymiz
aniqlash = (
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