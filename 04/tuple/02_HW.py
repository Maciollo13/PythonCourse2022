# Stwórz krotkę.
# Znajdź powtarzające się elementykrotki
# Wyświetl je.
a = 0
tuple1 = (2, 3, 5, 6, 27, 4, 76, 2, 3)
list1 = list(tuple1)
print(list1)
list1 = sorted(list1)
for i in list1:
    a = list1.count(i)
    if a > 1:
        list1.remove(i)
tuple1 = tuple(list1)
print(tuple1)
# ------or-------
print("---------------------------")
tuple2 = (1, 2, 3, 2, 56, 5, 1, 2 )
print(tuple2)
set1 = set(tuple2)
tuple2 = tuple(set1)
print(tuple2)