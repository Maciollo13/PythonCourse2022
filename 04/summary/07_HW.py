example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
set1 = {}
list1 = []
set1 = set(example_list)
list1 = list(set1)
list1.sort()
print(list1)
a = len(list1)
print("Minimalna liczba to ", min(list1))
print("Maxymalna liczba to ", max(list1))