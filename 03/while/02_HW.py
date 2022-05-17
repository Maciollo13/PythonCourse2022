secret_num = 7
while True:
    num = int(input("Podaj liczbę od 1 - 20. "))
    if num != secret_num and num <= 20 :
        print("Zgaduj dalej!")
    elif num > 20:
        print("To nie jest liczba od 1-20.")
    else:
        break
print("Gratulacje, zgadłeś!")

print("-----------ALBO----------")
num1 = int(input("Podaj liczbę od 1 - 20. "))
while num1 != secret_num:
    if num1 > 20:
        print("To nie jest liczba z przedziału 1 - 20.")
    print("Zgaduj dalej.")
    num1 = int(input("Podaj liczbę od 1 - 20. "))
print("Zgadłeś!")