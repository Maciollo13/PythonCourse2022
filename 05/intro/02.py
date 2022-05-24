#def even_number(number):
    #if number % 2 == 0:
   #     print("Liczba jest parzysta.")
  #  else:
 #       print("liczba nie jest parzysta")


#user_number = int(input("Podaj liczbe"))
#even_number(user_number)



def even_number(number):
    return number % 2 == 0

user_number = int(input("Podaj liczbę: "))
result = even_number(user_number)
if result == False:
    print("Nie jest parzysta")
else:
    print("Jest parzysta")
