
def BMI_counter(m, h):
    BMI = float(m) / (float(h) ** 2)
    if BMI <= 18.49:
        return "Underweight"
    elif BMI <= 24.99:
        return "Normal weight"
    elif BMI < 30.00:
        return "Overweight"
    else:
        return "Obesity"

def main():
    masa = input("Podaj swoja mase ")
    wzrost = input("Podaj swoj wzrost w m ")


    result = BMI_counter(masa, wzrost)
    print(result)

if __name__ == "__main__":
    main()
