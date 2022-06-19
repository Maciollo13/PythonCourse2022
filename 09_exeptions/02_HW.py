
tup1 = (1, 2, 6, 45, 0, 56, 40, 9)
index = int(input("Podaj index"))
value = int(input("Podaj value"))
try:
    tup1[index] = tup1[value]
except IndexError:
    print("Nie ma indexu " + index)
except TypeError:
    l1 = list(tup1)
    l1[index] = value
    tup1 = tuple(l1)
print(tup1)