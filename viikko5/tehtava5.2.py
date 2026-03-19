#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
#tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista
#viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
#lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True


luvut = []

while True:
    luku = input("Syötä luku, tyhjä merkkijono lopettaa:")
    if luku == "":
        break

    if luku != "":

        luku = int(luku)
        luvut.append(luku)

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
print(luvut[:5])





