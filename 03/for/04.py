number = int(input("Podaj liczbę nie większą niż 8  "))
start = 1
if number > 8:
    print ("Cyfra musi byc nie większa niż 8 ")
else:
    for i in range(start, number):
        start = start + (start * i)
        print(start)