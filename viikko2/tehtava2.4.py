#aloitetaan nimeämällä muuttujat, joiden avulla kysytään 3 numeroa

numero1 = float(input("Anna ensimmäinen numero"))
numero2 = float(input("Anna toinen numero"))
numero3 = float(input("Anna kolmas numero"))

#sitten nimetään summa, tulo ja keskiarvo

summa = numero1 + numero2 + numero3
tulo = numero1*numero2*numero3
keskiarvo = summa / 3

#printataan että saadaan vastaukset

print("Lukujen summa on:", summa)
print("Lukujen tulo on:", tulo)
print("Lukujen keskiarvo on:", keskiarvo)

