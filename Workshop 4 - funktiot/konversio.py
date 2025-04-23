#konversio funktio
def konversio( celsius ):
    f = celsius * (9/5) + 32
    print(f"Lämpötila on Fahrenheiteina: [{f:^10.2f}]")
    # Palauttaa arvon kutsujalle
    return f

# Kysy käyttäjän input
lampotila = float(input("Anna lämpötilan Celsius-asteina: "))

# Kutsu funktiota joka hoitaa konversion
tulos = konversio( lampotila )

# Tutkitaan palautusarvoa
print("Palautusarvo: ", tulos)