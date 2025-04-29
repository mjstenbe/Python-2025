try:
    with open("example2.txt") as my_file:
        for line in my_file:
            print(line)

except IndexError:
    print("Indeksi meni rikkI!")

except FileNotFoundError:
    print("Tiedostoa ei löydy!")
    
except Exception:
    print("There was an error when reading the file.")
