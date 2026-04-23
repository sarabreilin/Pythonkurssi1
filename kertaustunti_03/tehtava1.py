#tehtava 1

arvot = {"John" : ["John", 30, "Engineer"],
"Emily" : ["Emily", 25, "Artist"],
"Anna" : ["Anna", 22, "Student"]}

#Hae ja tulosta: Johnin nimi ja ikä sekä Emilyn ammatti

print(f"Nimi ja ikä on: {arvot['John'][0]} {arvot['John'][1]} ja Emilyn ammatti on: {arvot['Emily'][2]}")

#Muokkaa sanakirjaa: vaihda Annan ammatiksi "Teacher" ja lisää uusi avain-arvo-pari
#"James" listalla ["James", 28, "Writer"].

arvot["Anna"][2] = "Teacher"

arvot["James"] = ["James", 28, "Writer"]




#Lisää uusi merkintä: "Sophia", jonka ikä on 35 ja ammatti lääkäri.

arvot["Sophia"] = ["Sophia", 35, "Doctor"]


#Poista yksi merkintä: poista "Emily" sanakirjasta.

del arvot["Emily"]


#Tulosta lopullinen sanakirja.

print(arvot)


