#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina
#saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
#Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def parittomat(numero):
    parilliset = []
    for luku in numero:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

alk_lista = [2,7,4,9,2,44,143,773,24,97,12,46,89]
poistettu = parittomat(alk_lista)

print("Alkuperäinen lista on:", alk_lista)
print("Karsittu lista on:", parittomat(alk_lista))

