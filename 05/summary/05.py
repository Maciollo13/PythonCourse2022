import random

def comp_pick():
    return int(random.randrange(1,100))

def player_choice():
    return int(input("Podaj liczbę od 1 - 100  "))

def range_of_choice(comp):
    ran = comp - 10
    ran1 = comp + 10
    return range(ran , ran1)

def heat(range, player,comp):
    if player in range:
        return "ciepło"
    elif player == comp:
        return True
    else:
        return "zimno"


def game():
    computer = comp_pick()
    player = player_choice()
    range1 = range_of_choice(computer)
    while True:
        result = heat(range1,player, computer)
        if result == True:
            break
    print("Wygrałeś")

game()