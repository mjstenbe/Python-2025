ika = int(input("Anna ikä: "))

# Jos ikä on pienempi kuin 0 tai suurempi kuin 150, tulostetaan ”Virheellinen ikä!”
if ika < 0 or ika > 150:
    print("Virheellinen ikä!")

# Jos ikä on alle 6 tulostetaan ”Esikoululainen”
elif ika > 4 and ika < 6:
    print("Esikoululainen.")

# Jos ikä on tasan 14 tulostetaan ”Haastava ikä”

elif ika == 14 or ika == 15:
    print("Haastava ikä!")

# Jos ikä on 16  - 18 tulostetaan ”Lähes aikuinen”
elif ika >= 16 and ika <= 18:
    print("Lähes aikuinen.")

# Jos ikä on suurempi kuin 18, mutta pienempi kuin 30 tulostetaan,”Olet täysi-ikäinen, muttet vielä keski-iän kriisissä”.
elif ika > 18 and ika < 30:
    print("Olet täysi-ikäinen, muttet vielä keski-iän kriisissä.")

# Jos ikä on suurempi tai yhtä suuri kuin 30, mutta pienempi kuin 45 tulostetaan: 
elif ika >= 30 and ika < 45:
    print("Olet keski-iässä")

# Jos ikä on suurempi kuin 45 mutta alle 65 tulostetaan ”Vielä ehtii ennen eläkettä!”
elif ika > 45 and ika < 65:
    print("Vielä ehtii ennen eläkettä!")

# Muuten ohjelma tulostaa ”Olet eläkeläinen”.

else:
    print("Olet eläkeläinen.")