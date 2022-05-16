grade1 = float(input("Podaj ocenę w skali 1-10: "))
grade2 = float(input("Podaj ocenę w skali 1-10: "))
grade3 = float(input("Podaj ocenę w skali 1-10: "))
sum = (grade1 + grade2 + grade3) / 3
if sum > 7:
    print("Bardzo dobra.")
elif sum >=5 and sum <= 7:
    print("Przeciętna.")
else:
    print("Nie warta uwagi.)