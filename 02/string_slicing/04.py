title = input("Podaj tytuł książki ")
author = input("Podaj autora książki ")
page = input("Podaj ilość stron ")
s1 = title.isalpha()
print(f"Czy tytuł zawiera same litery? {s1}")
s2 = page.isdigit()
print(f"Czy liczba stron jest wartością liczbową? {s2}")
title =title.capitalize()
author = author.capitalize()
print(title, author)
book = title + " " + author + " " + page
print(book)
len_book = len(book)
print(len_book)