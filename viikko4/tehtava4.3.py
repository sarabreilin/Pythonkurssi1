#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon
#lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
from enum import nonmember

teksti = float(input("Syötä luku: "))

pienin = None
suurin = None

while teksti != "":
    luku = float(teksti)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

    teksti = input("Syötä luku: ")

print("Suurin luku:", suurin)
print("Pienin luku:", pienin)





