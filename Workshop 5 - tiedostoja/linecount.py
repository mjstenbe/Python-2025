with open("example.txt") as new_file:
    count = 0
    total_length = 0

    # Käydään jokainen rivi läpi
    for line in new_file:
        # Poistetaan rivinvaihto kosmeettisista syistä
        line = line.replace("\n", "")
        # Kasvatetaan rivimäärää
        count += 1
        print("Line", count, line)
        # Lasketaan rivin merkkimäärä
        length = len(line)
        total_length += length
print("Total length of lines:", total_length)