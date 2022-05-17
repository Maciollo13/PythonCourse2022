import random
num = int(random.randrange(1,100))
tries = 0
ran1 = num - 10
ran2 = num + 10
while tries < 7:
    player_choice = int(input("Wprowadź liczbę "))
    if player_choice >= ran1 and player_choice <= ran2:
        print("Ciepło")
        tries += 1
    else:
        print("Zimno")
        tries += 1
    if player_choice == num:
        break
if tries > 6:
    print(f"Przegrałeś. Liczba o której myślalem to {num}")
else:
    print(f"Wygrałeś! Liczba {num} to liczba o której myśle")