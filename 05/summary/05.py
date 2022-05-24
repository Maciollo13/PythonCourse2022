import random

def comp_pick():
    return int(random.randrange(1,100))

def player_choice():
    return int(input("Podaj liczbę od 1 - 100  "))

def range_of_choice(comp,player):
    ran = comp - 10
    ran1 = comp + 10
    for i in range(ran,ran1):
        if player == i:
            return True



def game():
    computer = comp_pick()
    while True:
        player = player_choice()
        if player == computer:
            break
        elif range_of_choice(computer,player) == True:
            print("Ciepło")
        else:
            print("Zimno")


    print("Wygrałeś")

game()