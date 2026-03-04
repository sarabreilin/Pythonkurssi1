#tehtävä 1

nimi = input("Mikä on nimesi?")


if nimi != "Matti":
    hinta = 5.90
    annos = int(input("Montako keittoannosta?"))
    kokonaishinta = hinta*annos
    print("Kokonaishinta on", kokonaishinta)
    print("Seuraava, kiitos!")


else:
    print("Seuraava, kiitos!")

