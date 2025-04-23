def viesti():
    print("Hoi Maailma")
    print("Vi ska bada bastu!")

def tulostaVastaus( viesti ):
    print( viesti )

def kysyKuulumiset():
    kuulumiset = input("Mitäpä kuuluu?")
    if (kuulumiset == "hyvää"):
        tulostaVastaus("Tosi Hyvää!")
    else:
        tulostaVastaus("Ei niin hyvää!")

print("Ohjelma alkaa!")
viesti()
kysyKuulumiset()
viesti()
print("Ohjelma päättyy!")
