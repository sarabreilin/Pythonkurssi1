raha = float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("Tässä kahvisi ole hyvä!")

else:
    puuttuva = 5 - raha
    print("Sori, sinulta puuttuu", puuttuva)

print("Kiitos hei!")

#else lauseke ei voi olla olemassa ilman if-lauseketta, ei siis toimi yksinään

