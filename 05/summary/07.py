# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.

# Co wiemy o tych numerach tych kart?

# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.

# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.

# American Express card numbers start with 34 or 37 and have 15 digits.

def is_card_number(number):
    return (number.isdigit() and 13 >= len(number) <= 16 ) # this returns true or false without if/else

def card_lenth(number):
    return int(len(number))

def is_visa(number,length):
    return length in [13,16] and number[0] == "4"

def is_master(number, length)
    return length == 16 and (51 <= int(number[0:2]) <= 55 or 2221 <= int(number[0:4] <= 2720))


def is_americanexpress(number,length)
    return length == 15 and number.startswith((34,37))

def main():
    while True
        number = input("Podaj numer karty")
        if is_card_number(number):
            break
        else:
    length = card_lenth(number)
    print("Visa " + is_visa(number, length))
    print("MasterCard " + is_master(number, length))
    print("AmericanExpress " + is_americanexpress(number, length))
    pass

main()

