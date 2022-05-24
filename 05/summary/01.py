
def BMI_counter(m, h):
    BMI = float(m) / (float(h) ** 2)
    if BMI <= 18.49:
        return "Niedowaga"
    elif BMI <= 24.99:
        return "Waga normalna"
    else:
        return "Nadwaga"


masa = input("Podaj swoja mase ")
wzrost = input("Podaj swoj wzrost w m ")


result = BMI_counter(masa, wzrost)
print(result)