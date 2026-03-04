#tehtävä 3

kokonaisluku = int(input("Anna kokonaisluku:"))

while kokonaisluku > 0:
    from math import sqrt
    print(sqrt(kokonaisluku))
    kokonaisluku = int(input("Anna kokonaisluku:"))

if kokonaisluku < 0:
    print("Virheellinen numero!")
    kokonaisluku = int(input("Anna kokonaisluku:"))
