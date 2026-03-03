#tuodaan random kirjastosta

import random

#arvotaan luku väliltä 1-10 (tämä vaihe ennen while-silmukkaa, muuten numero muuttuu joka kierroksella)

luku = random.randint(1,10)

# arvaus

arvaus = int(input("Arvaa numero väliltä 1-10:"))

#käytetään while-silmukkaa

while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus!")
    else:
        print("Liian pieni arvaus!")

    arvaus = int(input("Arvaa numero väliltä 1-10:"))


print("Oikea vastaus!")

