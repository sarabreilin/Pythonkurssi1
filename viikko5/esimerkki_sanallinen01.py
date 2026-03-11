#luo ohjelma, joka kysyy käyttäjältä hänen lempivärinsä. Tarkista, löytyykö lempiväri
#ennalta määritellystä värilistasta, ja vastaa sen mukaisesti. Määrittele lista itse

varilista = ["punainen", "sininen", "keltainen", "vihreä"]
lempivari = input("Mikä on lempivärisi?")

while True:

    if lempivari in varilista:
        print("Väri on värilistassa")

    else:
        print("Väriä ei löydy listasta")

    lempivari = input("Mikä on lempivärisi?")







