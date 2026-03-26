#Päivitä laskin.py -tiedostosi (esimerkki löytyy OMA:sta, dokumentit-kansiosta) niin,
#että laskutoimitukset suoritetaan niitä vastaavilla funktioilla. Määrittele funktio itse.

import math

def summa(a, b):
    return a+b


def erotus(a, b):
    return a - b


def tulo(a, b):
    return a * b


def osamaara(a, b):
    if b == 0:
        return "Virhe (nollalla jako)"
    return a / b


while True:

    laskutoimitus = input("Valitse laskutoimitus:")
    luku1 = float(input("Anna ensimmäinen numero:"))
    luku2 = float(input("Anna toinen numero:"))

    if laskutoimitus == "summa":
        print(summa(luku1, luku2))

    elif laskutoimitus == "erotus":
        print(erotus(luku1, luku2))

    elif laskutoimitus == "tulo":
        print(tulo(luku1, luku2))

    elif laskutoimitus == "osamäärä":
        print(osamaara(luku1, luku2))

    else:
        break