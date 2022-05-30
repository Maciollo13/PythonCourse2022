import random

def comp_pick():
    computer = random.choice(["k","p","n"])
    return computer

def player_pick():
    print("Wybierz: \n K - Kamien \n P - Papier \n N - Nożyce")
    player = input("")
    player = player.lower()
    player = player[0]
    return player


def game():
    player_score = 0
    comp_score = 0
    ties = 0
    counter = 0
    tries = int(input("Podaj liczbę rund: "))
    while counter < tries:
        computer = comp_pick()
        player = player_pick()
        print("Komputer wybrał "+ computer.capitalize())
        if computer == player:
            print("Remis!")
            ties += 1
        elif (player == "k" and computer == "n") or (player == "p" and computer == "k") or (player == "n" and computer == "p"):
            print("Wygrałeś")
            player_score += 1
        else:
            print("Przegrałeś")
            comp_score += 1
        counter += 1
    if comp_score > player_score:
        print(f"Przegrałeś! {comp_score} do {player_score} i {ties} remisów")
    elif player_score > comp_score:
        print(f"Wygrałeś! {player_score} do {comp_score} i {ties} remisów")
    else:
        print(f"Remis! {player_score} do {comp_score} i {ties} remisów")

def end_game():
    print("Continue?")
    print("Type: \n Yes \n No")
    choice = input("--> ")
    choice = choice.casefold()
    if choice == "yes":
        return True
    elif choice == "no":
        return False



def difficulty_level():
    print("Difficulty level: \n A - Smart \n B - Stupid \n")
    player_choice = input("----> ")
    player_choice = player_choice.casefold()
    if player_choice == "a":
        print("jeszcze nie ma")
    elif player_choice == "b":
        game()
        result = end_game()
        if result == True:
            game()
        else:
            return False
        print("Continue?")
    else:
        print("Wybierz z Podanych")
        return


def game_screen():
    print("Welcome! \n S - start \n P - Difficulty level \n Q - Quit")
    player_choice = input("----> ")
    player_choice = player_choice.casefold()
    while True:
        if player_choice == "s":
            game()
            result = end_game()
            if result == True:
                continue
            else:
                break
        elif player_choice == "p":
            difficulty_level()
            break
        else:
            break

game_screen()
