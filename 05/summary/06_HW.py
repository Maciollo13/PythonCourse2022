import random

def comp_pick():
    computer = random.choice(["k","p","n"])
    return computer

def player_pick():
    player = input("Wybierz: Kamień, Papier, Nożyce ")
    player = player.lower()
    player = player[0]
    return player

def player_stone(comp):
    if comp == p:
        return False


def game():
    player_score = 0
    comp_score = 0
    ties = 0
    counter = 0
    tries = int(input("Podaj liczbę rund: "))
    while counter <= tries:
        computer = comp_pick()
        player = player_pick()
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

game()