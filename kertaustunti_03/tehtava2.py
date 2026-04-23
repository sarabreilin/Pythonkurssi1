#tehtava2

#Luo sanakirja, jossa oppilaiden nimet ovat avaimina ja listat arvoina.
#Jokaisen listan tulee sisältää: [nimi, vuosiluokka, lempiaine]

arvot = { 'Siiri': ["Siiri", "8", "Liikunta"],
'Oona': ["Oona", "7", "Musiikki"],
'Sara': ["Sara", "9", "Historia"],}

#Hae ja tulosta yhden oppilaan vuosiluokka sekä toisen oppilaan lempiaine.

print(f"Oppilaan vuosiluokka on: arvot['Siiri'][2] ja oppilaan lempiaine on arvot['Oona'][3]")

#Muokkaa sanakirjaa vaihtamalla yhden oppilaan lempiaine.

arvot['Sara'][2] = "Matikka"

# Lisää uusi oppilas sanakirjaan
arvot['Anniina'] = ["Anniina", 4, "Äidinkieli"]

#Poista yksi olemassa oleva oppilas sanakirjasta.

del arvot['Sara']

#Tulosta päivitetty sanakirja.

print(arvot)


