tab1 = []
n = int(input("Wpisz liczbe elementów: "))
for i in range(0,n):
    ele = input()
    tab1.append(ele)
if tab1[0] == tab1[-1]:
    print("Są takie same")
else:
    print("Nie są takie same")

