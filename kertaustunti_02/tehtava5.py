#Kirjoita funktio nimeltä suurin_arvo, joka saa kolme argumenttia.
#Funktion tulee palauttaa näistä kolmesta suurin arvo.
#Kysy luvut käyttäjältä input-funktion avulla.

def suurin_arvo(a, b, c):
    return max(a, b, c)

eka = int(input("Syötä ensimmäinen arvo:"))

toka = int(input("Syötä toinen arvo:"))

kolmas = int(input("Syötä kolmas arvo:"))

suurin = (suurin_arvo(eka, toka, kolmas))
print("Suurin arvo on", suurin)






