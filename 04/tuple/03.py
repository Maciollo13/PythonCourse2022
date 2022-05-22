tuple = (2 , 3 , 6 , 7)
user = float(input("Podaj liczbę całkowitą: "))
flag = False
for i , v in enumerate(tuple):
    if user == v:
        print("znajduje sie na miejscu ", i)
        flag = True
        break
if flag == False:
    print("Nie znajduje sie")




