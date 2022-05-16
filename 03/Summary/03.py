numbers = input("Wpisz ciąg symboli: ")
len_numbers = len(numbers)
print(len_numbers)
num = 0
large = 0
small = 0
marks = 0
for i in numbers:
    if i.isdigit():
        num += 1
    if i.isalpha() and i.isupper():
        large += 1
    if i.isalpha() and i.islower():
        small += 1
    if not i.isalpha() and not i.isalnum():
        marks += 1
print(f"Małych liter jest {small} Dużych liter jest {large} Cyfr jest {num} Znaków jest {marks}")

