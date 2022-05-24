# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.
n = 0
a = 1
list1 = []
my_list = []
tab = []
while n < 10:
    for i in range(1,11):
        my_list.append(i*a)

    my_list = [my_list]
    tab.append(my_list)

    my_list.clear()
    n += 1
    a += 1



print(tab)




