#tehtävä 2

tehdyt_tunnit = float(input("Kerro tehdyt työtunnit:"))
tuntipalkka = float(input("Kerro tuntipalkka:"))
viikonpaiva = input("Kerro viikonpäivä:")

paivapalkka = tuntipalkka * tehdyt_tunnit

if viikonpaiva != "sunnuntai":
    print("Päiväpalkkasi on", paivapalkka)

else:
    print("Päiväpalkkasi on", paivapalkka*2)


