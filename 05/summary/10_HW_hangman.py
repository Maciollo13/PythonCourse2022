import random

def computer_draw():
    list_of_words = ["prize", "drowing", "energy", "life", "beer"]
    computer_word = random.choice(list_of_words)
    return computer_word

def word_camuflage(word):
    camuflage = ""
    for i in word:
        i = "-"
        camuflage += i
    return camuflage

def player_choice():
    choice = input("Podaj literę: ")
    choice = choice.casefold()
    choice = choice[0]
    return choice

def word_check(player, word, camuflage):
    blank_word = camuflage
    for i , v in enumerate(word):
        if v == player:
            blank_word[i] = v
    return blank_word

def true_check(player_list, camuflage):
    if player_list == camuflage:
        pass



def Hangman():
    computer_choice = list(computer_draw())
    print(word_camuflage(computer_choice))
    camuflage = list(word_camuflage(computer_choice))
    while True:
        player_letter = player_choice()
        print(camuflage)
        temporary_word = word_check(player_letter, computer_choice, camuflage)
        print(str(camuflage))
        word = temporary_word
        print(str(temporary_word))
        if str(camuflage) == str(word):
            print("Trafiłeś")
        else:
            print("Pudło")
        camuflage = temporary_word
        if temporary_word == computer_choice:
            temporaty_word = str(temporary_word)
            break

    print(f"Gratulacje! Wygrałeś to słowo to {temporaty_word}")

Hangman()