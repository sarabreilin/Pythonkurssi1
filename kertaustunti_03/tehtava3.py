#tehtävä3

#Luo sanakirja nimeltä kirjasto, jossa avaimina ovat kirjojen nimet (merkkijonoja) ja arvoina
#listat, jotka sisältävät seuraavat tiedot: [kirjoittaja, julkaisuvuosi, genre]

kirjasto = {'Harry Potter ja viisasten kivi': ["JK Rowling", 1997, "fantasia"],
            'Narnian tarinat':["CS Lewis", "1950", "fantasia"],
            'Kuolema Niilillä':["Agatha Cristhie", "1940", "dekkari"]}

#Hae ja tulosta yhden kirjan kirjoittaja sekä toisen kirjan genre.

print(f"Kirjan on kirjoittanut {kirjasto['Harry Potter ja viisasten kivi'][0]} ja toisen kirjan genre on {kirjasto['Narnian tarinat'][2] }")

#Muokkaa: vaihda yhden kirjan genre.

kirjasto['Narnian tarinat'][2] = "tietokirjallisuus"

#Lisää uusi kirja sanakirjaan.

kirjasto['Uusi testamentti'] = ["Kolme viisasta miestä", "50 jkr", "fiktio"]

#Poista yksi olemassa oleva kirja sanakirjasta.

del kirjasto['Kuolema Niilillä']

#Tulosta päivitetty sanakirja.

print(kirjasto)



