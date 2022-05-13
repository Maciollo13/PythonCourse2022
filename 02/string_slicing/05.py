p1 = input("Podaj słowo: ")
p1 = p1.casefold()
p1 = p1.replace(' ', "")
p2 = p1[::-1]
print(p1,p2)
print(f"Czy podane zdanie jest palindromem? {p1 == p2}")