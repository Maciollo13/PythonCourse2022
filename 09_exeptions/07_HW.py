import random

def get_quote(filename):
    try:
        with open(f'{filename}.txt',encoding="utf-8") as fopen:
            content = fopen.readlines()
    except FileNotFoundError:
        print("There is no such file. Try again!")
    quote = random.choice(content)
    return quote


def show(quote):
    quote = quote.strip('\n')
    quote = quote.split(' - ') # [cytat, autor]
    lenth = len(quote[0]) + 20

    print('\nQuote of the day is:\n')
    print('*' * lenth)
    print(quote[0].center(lenth))
    print(f'~ {quote[1]} ~'.center(lenth))
    print('*' * lenth)


def main():
    filename = input("Your file name: ")
    quote = get_quote(filename)
    show(quote)

if __name__ == "__main__":
    main()