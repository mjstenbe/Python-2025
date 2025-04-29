import statistics
import matplotlib.pyplot as plt

# Luodaan tiedosto ja käydään sitä läpi rivi kerrallaan
with open("data.csv") as new_file:
    for line in new_file:
        # Poistetaan rivinvaihdot
        line = line.replace("\n", "")
        # Jaetaan tietokentät taulukkoon puolipisteellä eroteltuna
        parts = line.split(";")
        # Poimitaan taulukon eka alkio eli nimi
        name = parts[0]
        # Poimitaan taulukon loput alkiot eli numerot
        grades = parts[1:]
        # Tulostetaan nimi ja numerot
        print("Name:", name)
        print("Grades:", grades)
        # Muutetaan numerot merkeistä kokonaisluvuiksi
        for i in range(len(grades)):
            grades[i] = int(grades[i])

    # Lasketaan keskiarvo ja tulostetaan se
    print("Mean: ", statistics.mean(grades))
    print("Sum: ", sum(grades))
    print("Max: ", max(grades))
    print("Min: ", min(grades)) 
    print("Median: ", statistics.median(grades))
    # Piirrä kuvaaja
    plt.plot(grades)
    plt.show()     
    labels = ['A', 'B', 'C']
    values = [10, 15, 7]
    # Piirrä pylväskaavio
    plt.bar(labels, values)
    plt.title("Pylväskaavio")
    plt.show()
   