"""
Kirjoita ohjelma, joka pyytää käyttäjältä päivän (1–31), kuukauden (1–12) ja vuoden. 
Tarkista, onko annettu päivämäärä kelvollinen. Huomioi seuraavat asiat:
•	Kuukaudet, joissa on 30 päivää: huhtikuu (4), kesäkuu (6), syyskuu (9), marraskuu (11).
•	Helmikuussa (2) on normaalisti 28 päivää, mutta karkausvuonna 29 päivää.

"""
# Kirjoita ohjelma, joka pyytää käyttäjältä päivän (1–31), kuukauden (1–12) ja vuoden. 
paiva = int(input("Anna päivä: "))
kk = int(input("Anna kuukausi: "))
vuosi = int(input("Anna vuosi: "))

# Suljetaan pois virheelliset kuukaudet
if kk < 1 or kk > 12:
    print("Virheellinen kuukausi!")

# Kuukaudet, joissa on 30 päivää: huhtikuu (4), kesäkuu (6), syyskuu (9), marraskuu (11).
elif kk == 4 or kk == 6 or kk == 9 or kk == 11:
    if paiva < 1 or paiva > 30:
        print("Virheellinen määrä päiviä!")
# Helmikuu
elif kk == 2:
     if paiva < 1 or paiva > 28:
        print("Virheellinen määrä päiviä!")

# Oletetaan että muissa on 31 päivää
elif paiva != 31:
     print("Virheellinen määrä päiviä!")