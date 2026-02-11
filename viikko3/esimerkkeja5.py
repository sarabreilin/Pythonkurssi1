#monta vaihtoehtoa: elif-haara
#elif haaroja voi olla rajaton määrä, mutta vain yksi ajetaan

numero = int(input("Anna kokonaisluku:"))

if numero > 0:
    print("Luku on positiivinen")

elif numero < 0:
    print("Luku on negatiivinen")

else:
    print("Numero oli 0")

