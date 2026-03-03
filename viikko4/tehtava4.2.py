#ohjelma muuttaa tuumia senttimetreiksi niin kauan, kun käyttäjä syöttää negatiivisen luvun

#muuttujan tuuma arvoksi seuraava

tuuma = float(input("Syötä tuumat:"))


#muunnetaan tuumat senttimetreiksi

senttimetri = tuuma * 2.54

#while-rakenne

while tuuma >= 0:
    senttimetri = senttimetri + tuuma
    print(senttimetri)
    tuuma = float(input("Syötä tuumat:"))

