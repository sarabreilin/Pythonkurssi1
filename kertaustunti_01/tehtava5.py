#tehtävä 5 Laskin-ohjelma

import math

laskutoimitus = input("Valitse laskutoimitus:")

luku1 = float(input("Anna ensimmäinen numero:"))
luku2 = float(input("Anna toinen numero:"))


while True:
    if laskutoimitus == "yhteenlasku":
        print(luku1+luku2)

        laskutoimitus = input("Valitse laskutoimitus:")

        luku1 = float(input("Anna ensimmäinen numero:"))
        luku2 = float(input("Anna toinen numero:"))


    elif laskutoimitus == "vähennyslasku":
        print(luku1-luku2)

        laskutoimitus = input("Valitse laskutoimitus:")

        luku1 = float(input("Anna ensimmäinen numero:"))
        luku2 = float(input("Anna toinen numero:"))

    elif laskutoimitus == "kertolasku":
        print(luku1*luku2)

        laskutoimitus = input("Valitse laskutoimitus:")

        luku1 = float(input("Anna ensimmäinen numero:"))
        luku2 = float(input("Anna toinen numero:"))


    elif laskutoimitus == "jakolasku":
        print(luku1/luku2)

        laskutoimitus = input("Valitse laskutoimitus:")

        luku1 = float(input("Anna ensimmäinen numero:"))
        luku2 = float(input("Anna toinen numero:"))

    else:
        break

#jos haluat päästä helpommalla niin voi tehä näinkin :DDDD

while True:

    laskutoimitus = input("Valitse laskutoimitus:")
    luku1 = float(input("Anna ensimmäinen numero:"))
    luku2 = float(input("Anna toinen numero:"))

    if laskutoimitus == "yhteenlasku":
        print(luku1+luku2)

    elif laskutoimitus == "vähennyslasku":
        print(luku1-luku2)

    elif laskutoimitus == "kertolasku":
        print(luku1*luku2)

    elif laskutoimitus == "jakolasku":
        print(luku1/luku2)

    else:
        break

#voi tehdä näin, koska while-looppi toistaa sen alle listatut jutut automaattisesti ja palaa alkuun, joten ei tarvitse turhaan toistaa samoja kysymyksiä









