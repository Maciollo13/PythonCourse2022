def is_card_number(number):
    return (number.isdigit() and 13 >= len(number) <= 16 ) # this returns true or false without if/else

def card_lenth(number):
    return int(len(number))

def is_visa(number,length):
    return length in [13,16] and number[0] == "4"

def is_master(number, length)
    return length == 16 and (51 <= int(number[0:2]) <= 55 or 2221 <= int(number[0:4] <= 2720))

def check_card(number):
    if is_visa(number):
        save('visa', number)
    elif is_master(number):
        save('mastercard', number)
    elif is_americanexpress(number):
        save('amex', number)
    else:
        save('unknown_card', number)


def read():
    with open('cards.txt') as fopen:
        content = fopen.readlines()
    return content

def save(cardtype, number):
    with open(f'{cardtype}.txt', 'a') as fopen:
        fopen.write(f'{number}\n')

def is_americanexpress(number,length)
    return length == 15 and number.startswith((34,37))

def main():
    content = read()

    for i in content:
        i = i.replace(' ', "").replace("\n", "")
        check_card(i)

    print("Karty zostały dodane")



    length = card_lenth(number)
    print("Visa " + is_visa(number, length))
    print("MasterCard " + is_master(number, length))
    print("AmericanExpress " + is_americanexpress(number, length))
    pass

main()
