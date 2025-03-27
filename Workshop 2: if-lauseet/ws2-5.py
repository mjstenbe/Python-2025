# Pyydetään käyttäjältä päivä, kuukausi ja vuosi
paiva = int(input("Anna päivä: "))
kk = int(input("Anna kuukausi: "))
vuosi = int(input("Anna vuosi: "))

# Tarkistetaan, onko kuukausi validi
if kk < 1 or kk > 12:
    print("Virheellinen kuukausi!")

elif kk == 4 or kk == 6 or kk == 9 or kk == 11:  # Kuukaudet, joissa on 30 päivää
    if paiva < 1 or paiva > 30:
        print("Virheellinen määrä päiviä!")
    else:
        print("Kelvollinen päivämäärä.")

elif kk == 2:  # Helmikuu (28 päivää, ei tarkisteta karkausvuotta)
    if paiva < 1 or paiva > 28:
        print("Virheellinen määrä päiviä!")
    else:
        print("Kelvollinen päivämäärä.")
        
elif paiva < 1 or paiva > 31:  # Kuukaudet, joissa on 31 päivää
    print("Virheellinen määrä päiviä!")
else:
    print("Kelvollinen päivämäärä.")