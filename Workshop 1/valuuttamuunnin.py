# Tekstin tulostaminen keskitettynä
#  txt = "banana"
# x = txt.center(30, "O")
# print(x)

otsikko = "* Valuuttamuunnin *"
print("******************************")
print(f"{otsikko:^30s}")
print("******************************")
kurssi = float(input("Anna dollarin kurssi euroina:"))
raha = float(input("Anna rahan määrä euroina:"))
print(f"Rahan arvo on dollareina: {raha/kurssi:^10.2f}. ")
print("******************************")