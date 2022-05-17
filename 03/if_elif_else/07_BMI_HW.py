masa = input("Podaj swoja mase ")
wzrost = input("Podaj swoj wzrost ")
BMI = float(masa) / (float(wzrost)**2)
if BMI <= 18.49:
    print("Your BMI is:", round(BMI,2), "You have underweight!")
elif BMI <= 24.99:
    print("Your BMI is:", round(BMI,2), "Your weight is great!")
else:
    print("your BMI is:", round(BMI,2), "You have overweight!")
print("your BMI is:", round(BMI,2))
