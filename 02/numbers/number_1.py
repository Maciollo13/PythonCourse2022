distance = input("Podaj dlugość trasy w km >")
fuel_usage = input("Podaj spalanie na 100 km >")
fuel_price = input("Podaj cenę paliwa za litr >")

cost = (int(distance) * (float(fuel_usage) / 100)) * float(fuel_price)
print("Koszt podrózy wynosi:" , round(cost,2) , "PLN")
