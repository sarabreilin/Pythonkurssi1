#kirjoitetaan ohjelma, missä massa kysytään keskiaikaisten mittojen mukaan

#kirjoitetaan syötteet

leiviskat = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))


#muutetaan kaikki mitat luodeiksi

luodit_yht = leiviskat * 20 * 32 + naulat * 32 + luodit

# muutetaan grammoiksi
grammat_yht = luodit_yht * 13.3


# grammat ja kilot eritellään
kilot = int(grammat_yht // 1000)
grammat = grammat_yht % 1000

#tulostetaan
print("Massa on", kilot, "kilogrammaa ja", grammat, "grammaa.")

