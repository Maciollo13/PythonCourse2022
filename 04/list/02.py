tab1 = []
for i in range(0,10):
    ele = int(input("Wpisz liczbę: "))
    tab1.append(ele)
print(tab1)
for i in tab1:
    if i % 2 != 0:
        print(i, end=" ")

