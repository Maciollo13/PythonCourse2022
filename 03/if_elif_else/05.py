password = input("Podaj hasło: ")
if len(password) < 8:
    print("Hasło jest za krótkie!")
if password.isalpha():
    print("Hasło nie posiada cyfr!")
if password.isalnum() and ( password.isdigit() or  password.isalpha()):
    print("Hasło nie posiada cyfr i liter!")
if password.isalnum() and password.isupper():
    print("Hasło musi mieć jedna małą literę!")
if password.islower():
    print("Hasło musi miec jedną dużą literę!")

