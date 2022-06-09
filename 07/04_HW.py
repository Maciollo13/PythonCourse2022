import random

def get_quote(filename):
    with open(f'{filename}.txt',encoding="utf-8") as fopen:
        content = fopen.readlines()

    quote = random.choices(content, k=3)
    return quote


def show(quote):
    print('\nQuotes of the day is:\n')
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
    show(quote)

main()