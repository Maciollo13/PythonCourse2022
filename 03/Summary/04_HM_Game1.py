import random
print("Zagrajmy w grę. ")
print("Kamień (k) ")
print("Papier (p) ")
print("Nożyce (n)")
k = "Kamień"
p = "Papier"
n = "Nożyce"
print("Jeśli nie chcesz już grać, napisz \"stop\"")
player_rounds = int(input("Podaj liczbę rund: "))
tie = 0
player_score = 0
computer_score = 0
round = 0
while round != player_rounds:
    computer = random.choice([k, p, n])
    choice = input("Wybierz swoją broń! ")
    choice.casefold()
    choice = choice[0]
    if choice == "s":
        break
    if choice == "k":
        choice = k
    if choice == "p":
        choice = p
    if choice == "n":
        choice = n
    if choice == k or choice == n or choice == p:
        print("Komputer wybrał: " + computer)
        if choice == computer:
            print("Remis!")
            round += 1
            tie += 1
        elif (choice == k and computer == n) or (choice == p and computer == k) or (choice == n and computer == p):
            print("Wygrałeś!")
            player_score += 1
            round += 1
        else:
            print("Przegrałeś!")
            computer_score += 1
            round += 1
    else:
        print("Sprawdź czy dobrze wybrałeś.")
if player_score > computer_score:
    print(f"Wygrałeś {player_score} do {computer_score} i {tie} remisów")
elif player_score < computer_score:
    print(f"Przegrałeś {player_score} do {computer_score} i {tie} remisów")
else:
    print(f"Remis {player_score} do {computer_score} i {tie} remisów")