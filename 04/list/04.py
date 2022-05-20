tab1 = []
n = int(input("Podaj parzystą ilośc elementow: "))
mid1 = int(n/2)
mid2 = int((n/2)+1)
if n % 2 == 0:
    for i in range(0,n):
        ele = int(input("Podaj element"))
        tab1.append(ele)
    print(tab1)
    if tab1[mid1] == tab1[mid2]:
        v = tab1[mid1]
        print(f"Są takie same o wartości {v}")
    else:
        print("Nie są takie same")
else:
    print("Miała być parzysta")