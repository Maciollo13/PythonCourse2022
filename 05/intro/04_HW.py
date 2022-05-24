def even_number(l1):
    even_list = []
    for i in l1:
        a = i % 2
        if a == 0:
            even_list.append(i)
    return even_list

def user_list(user_input):
    user_input = list(user_input.split(" "))
    user_l = []
    for i in user_input:
        user_l.append(int(i))
    return user_l

def funcion():
    user_input = input("Podaj liczby do listy ")
    user = user_list(user_input)
    even_list = even_number(user)
    print("liczy parzyste to", *even_list)

funcion()
