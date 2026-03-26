# Kirjoita ohjelma, joka tulostaa kertotaulun käyttäjän antamalle numerolle välillä 1-10.

luku = int(input("Anna luku:"))

for i in range(1, 11):
    print(i * luku)

