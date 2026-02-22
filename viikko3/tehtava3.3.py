#kirjoitetaan kysymykset

hemoglobiiniarvo = float(input("Mikä on hemoglobiiniarvosi (g/l)?"))
sukupuoli = input("Oletko nainen vai mies?")

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 135:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

