# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat:
# “tak, liczba x znajduje się w zadanym zakresie”,
# “nie, liczba x jest z poza zakresu”.
import random
def range_check(first_number, last_number,number):
    number = number
    for i in range(first_number,last_number):
        if i == number:
            return True

def player_pick_lside():
    number = int(input("Podaj początkową liczbe zakresu: "))
    return number

def player_pick_rside():
    number = int(input("Podaj ostatnią liczbę zakresu: "))
    return number

def comp_pick():
    computer = random.randint(1, 100)
    return computer

def funcion():
    computer = comp_pick()
    player_lside = player_pick_lside()
    player_rside = player_pick_rside()
    flag = range_check(player_lside, player_rside, computer)
    if flag == True:
        print(f"tak, liczba {computer} znajduje się w zadanym zakresie")
    else:
        print(f"nie, liczba {computer} jest z poza zakresu")

funcion()