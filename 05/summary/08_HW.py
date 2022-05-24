def car_dict():
    d1 = {
        "Marka" : "Toyota",
        "Model" : "Avensis",
        "Rocznik" : 1997,
        "Czy Oryginalny" : False
    }
    return d1

def vintage_car():
    print(car_dict())
    car_list = list(car_dict().values())
    car_original = original()
    if car_original == True :
        if 2022 - car_list[2] >= 25:
            print(f"Gratulacje! Twój samochód {car_list[0]} może być zarejestrowany jako zabytek.")
        else:
            print(f"Twój samochód {car_list[0]} jest jeszcze zbyt młody.")
    else:
        print("Twój samochód nie ma oryginalnych części.")

def original():
    car_list = list(car_dict().values())
    if car_list[-1] == False:
        return False
    else:
        return True

vintage_car()