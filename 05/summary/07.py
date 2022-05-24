def car_dict():
    d1 = {
        "Marka" : "Toyota",
        "Model" : "Avensis",
        "Rocznik" : 1999
    }
    return d1

def vintage_car():
    print(car_dict())
    car_list = list(car_dict().values())
    if 2022 - car_list[2] >= 25:
        print(f"Gratulacje! Twój samochód {car_list[0]} może być zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {car_list[0]} jest jeszcze zbyt młody.")
vintage_car()