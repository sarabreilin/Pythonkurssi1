#listat ja alkiot

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
#arvot erotettu pilkuilla, ja koska arvot tekstiä, lainausmerkit

print(nimet[1])

#arvot alkaa aina nollasta, eli Viivi = 0

#voi laskea toiseen suuntaan, esim. -2, jolloin alkaa 1

#range-funktiossa aloituspiste huomioidaan, lopetuspistettä ei
print(nimet[1:3])

#tulostaa Ahmedin ja Pekan

#append-funktio lisää uuden arvon listalle

nimet.append("Matti")

#remove poistaa nimen listalta

nimet.remove("Pekka")


#jos halutaan arvolle tietty paikka listassa

nimet.insert(4,"Matti")



nimet2 = ["Allu", "Ninni"]

#jos halutaan yhdistää kaksi listaa

nimet.extend(nimet2)



#jos halutaan tietyn arvon indeksi tietää

indeksi = nimet.index("Olga")


#if voidaan tarkistaa, onko jokin tietty arvo listassa
#if (arvo) in (tietorakenne) --> tarkistaa onko tietty arvo tietorakenteen sisällä

if "Matti" in nimet:
    print("Matti löytyi")
else:
    print("Ei Mattia")


#listan voidaan järjestää (aakkosjärjestykseen)

nimet.sort()
print(nimet)

