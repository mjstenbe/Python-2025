print("SYÖTÄ HENKILÖTIEDOT")
print("--------------------")
# print('-' * 20)
print()
etunimet = input("Anna etunimet:")
sukunimi = input("Anna sukunimi: ")
email = input("Anna sähköpostiosoite: ")
osoite = input("Lähiosoite: ")
pnumero = input("Postinumero: ")
kaupunki = input("Kaupunki: ")
print()
print("HENKILÖN TIEDOT:")
print("-----------------")
print("NIMI:")
# Erilaisia tapoja tulostaa
# print(sukunimi,", ",etunimet) # Jättää ongelmallisia välejä
# print(sukunimi+", "+ etunimet)
print(f"\t{sukunimi}, {etunimet}")

loytyyko = email.find("@")
# print("Löytyikö merkki:", loytyyko)
if (loytyyko < 0):
    print("Sähköpostiosoite ei ole kelvollinen!")
else:
    print("SÄHKÖPOSTI: ")
    print(f"\t{email}")

print("OSOITE:")
print(f"\t{osoite}\n\t{pnumero}\n\t{kaupunki}")



