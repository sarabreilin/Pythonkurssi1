#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.


import random
summa = 0

arpakuutioiden_lkm = int(input("Mikä on arpakuutioiden lukumäärä?"))

for heitot in range(arpakuutioiden_lkm):
    heitot = random.randint(1,6)
    summa += heitot

print("Silmälukujen summa on", summa)
    