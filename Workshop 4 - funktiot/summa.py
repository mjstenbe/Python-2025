def summa(luku1, luku2):
    tulos = luku1 + luku2
    print("Summa on: ", tulos)
    return tulos # palauta muuttujan arvo

def summa(luku1, luku2, luku3):
    tulos = luku1 + luku2 + luku3
    print("Summa on: ", tulos)
    return tulos # palauta muuttujan arvo

# Kutsutaan summa-funktiota
a = summa(10, 20)
b = summa(50, 22342340, 345)
c = summa(3210, 23240, 234)

# Käytetään palautettuja arvoja uudelleen
summa(a, b, c)