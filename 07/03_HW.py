import random

def get_quote(filename):
    quote = []
    with open(f'{filename}.txt', encoding="UTF-8") as fopen:
        content = fopen.readlines()
    for i, v in enumerate(content):
        if i < 5:
            quote.append(v)
    print(quote)
    return quote


def show(quote):
    print('\nQuote of the day is:\n')
    for i in quote:
        i = i.strip('\n')
        i = i.split(' - ') # [cytat, autor]
        length = len(i[0]) + 20
        print('*' * length)
        print(i[0].center(length))
        print(f'~ {i[1]} ~'.center(length))
        print('*' * length)


def main():
    filename = input("Your file name: ")
    quote = get_quote(filename)
    print(quote)
    show(quote)

main()