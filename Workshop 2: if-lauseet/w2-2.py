# Pyydetään käyttäjältä kolme kokonaislukua
luku1 = int(input("Syötä eka luku: "))
luku2 = int(input("Syötä toka luku: "))
luku3 = int(input("Syötä kolmas luku: "))

kaikkiluvut = str(luku1)+str(luku2)+str(luku3) #  "9"

# Etsi suurin
if luku1 > luku2 and luku1 > luku3:
    print("Luku 1 on suurin", luku1)
    kaikkiluvut = kaikkiluvut.replace(str(luku1), "")
elif luku2 > luku1 and luku2 > luku3:
    print("Luku 2 on suurin: ", luku2)
    kaikkiluvut = kaikkiluvut.replace(str(luku2), "")
elif luku3 > luku1 and luku3 > luku2:
    print("Luku 3 on suurin:", luku3)
    kaikkiluvut = kaikkiluvut.replace(str(luku3), "")

# Etsi pienin
if luku1 < luku2 and luku1 < luku3:
    print("Luku 1 on pienin: ", luku1)
    kaikkiluvut = kaikkiluvut.replace(str(luku1), "")
elif luku2 < luku1 and luku2 < luku3:
    print("Luku 2 on pienin: ", luku2)
    kaikkiluvut = kaikkiluvut.replace(str(luku2), "")
elif luku3 < luku1 and luku3 < luku2:
    print("Luku 3 on pienin: ", luku3)
    kaikkiluvut = kaikkiluvut.replace(str(luku3), "")

print("Keskimmäinen luku on: ", kaikkiluvut)