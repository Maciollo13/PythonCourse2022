tab1 = []
for i in range(0,10):
    ele = int(input("Insert number: "))
    tab1.append(ele)
print(tab1)
print("Odd numbers: ")
for i in tab1:
    if i % 2 != 0:

        print(i, end=" ")

