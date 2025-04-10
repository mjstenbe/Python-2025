tunnus="mikamie"
salasana = 1233

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

if salasana == "1234" and tunnus == "mikamies":
    print("Tunnukset meni oikein!")

if salasana == "1234":
    print("Salasana meni oikein!")
if tunnus == "mikamies":
    print("Käyttäjätunnus meni oikein!")
else:
    print("Jompikumpi oli väärin")