
import math

def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija/2)/100
    pinta_ala = math.pi * sade**2
    return hinta / pinta_ala

d1 = float(input("Anna ensimmäisen pizzan halkaisija:"))
e1 = float(input("Anna ensimmäisen pizzan hinta:"))

d2 = float(input("Anna toisen pizzan halkaisija:"))
e2 = float(input("Anna toisen pizzan hinta:"))

hinta1 = yksikkohinta(d1, e1)
hinta2 = yksikkohinta(d2, e2)

print("Ensimmäisen pizzan hinta on:", hinta1,"€/m2")
print("Toisen pizzan hinta on:", hinta2, "€/m2")

if hinta1 > hinta2:
    print("Toinen pizza on halvempi.")

elif hinta1 < hinta2:
    print("Pizzat ovat samanarvoisia.")


