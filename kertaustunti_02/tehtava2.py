# Kirjoita ohjelma, joka pyytää käyttäjää syöttämään arvoja ja lisää ne listaan.
#Jokaisen lisäyksen jälkeen lista tulostetaan kahdella tavalla:
#lisäysjärjestyksessä ja pienimmästä suurimpaan järjestettynä.
#. Ohjelma lopettaa, kun käyttäjä syöttää 0


lista = []

while True:
    arvo = int(input("Syötä arvo, 0 lopettaa: "))

    if arvo == 0:
        break

    lista.append(arvo)

    print("Lista järjestyksessä:", lista)
    print("Lista pienimmästä suurimpaan:", sorted(lista))


