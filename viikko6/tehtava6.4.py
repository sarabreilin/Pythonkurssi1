#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan,
#kutsut funktiota ja tulostat sen palauttaman summan.


def laske_summa(numerot):
    summa = 0
    for n in numerot:
        summa += n
    return summa

def paaohjelma():
    luvut = [3, 5, 7, 99, 44, 24]
    tulos = laske_summa(luvut)
    print("Lukujen summa on", tulos)

paaohjelma()

