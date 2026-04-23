#Luo funktio create_point(x, y), joka palauttaa pisteen monikko-muodossa (x, y).
#Luo kaksi pistettä käyttämällä funktiota ja kysymällä arvot käyttäjältä.
#Luo funktio distance(p1, p2), joka laskee kahden pisteen välisen etäisyyden kaavalla:

#Kutsu distance-funktiota ja tulosta pisteiden välinen etäisyys.
#(Lisätehtävä) Pyöristä etäisyys kahden desimaalin tarkkuuteen käyttäen formatointia.

import math


def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

#ensimmäisen pisteen arvot
y1 = float(input("Anna ensimmäisen pisteen y-koordinaatti:"))
x1 = float(input("Anna ensimmäisen pisteen x-koordinaatti:"))
piste1 = create_point(x1, y1)


#toisen pisteen arvot
y2 = float(input("Anna toisen pisteen y-koordinaatti:"))
x2 = float(input("Anna toisen pisteen x-koordinaatti:"))
piste2 = create_point(x2, y2)

#etäisyyden laskeminen
etaisuus = distance(piste1, piste2)

print(f"Pisteiden {piste1} ja {piste2} välinen etäisyys on: {etaisuus}")






