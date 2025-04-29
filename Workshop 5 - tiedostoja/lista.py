text = "maitoa,leipää,piimää"
# Jaetaan teksti pilkkujen mukaan ja tallennetaan se listaan
words = text.split(",")
print(words[0])

# Tulostetaan lista
for word in words:
    print(word)