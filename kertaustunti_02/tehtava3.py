# Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän
# kuin 5 kirjainta.Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen.

lista = ["porkkana", "tomaatti", "kaali", "kiivi", "omena", "pupu", "talo"]

yli_viisi = 0

for i in lista:
    if len(i) > 5:
        yli_viisi += 1

print("Yli viisikirjaimisia sanoja on listassa yhteensä: ", yli_viisi)

