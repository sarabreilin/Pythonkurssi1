#merkitään taas ensin muuttujat, eli kanta ja korkeus

kanta = float(input("Mikä on suorakulmion kanta?"))

korkeus = float(input("Mikä on suorakulmion korkeus?"))

#merkitään sen jälkeen piiri ja pinta-ala omiksi muuttujikseen

pinta_ala = kanta * korkeus

piiri = kanta + kanta + korkeus + korkeus

#tulostetaan molempiin kysymyksiin vastaukset seuraavan lailla

print("Suorakulmion pinta_ala on:", pinta_ala)

print("Suorakulmion piiri on:", piiri)

