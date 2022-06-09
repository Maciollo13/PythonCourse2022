def get_longest_word():
    longest = 0
    word = []
    with open("inowkacja.txt", "r", encoding='utf-8') as fopen:
        content = fopen.read()
    content = content.replace("\n", " ")
    content = content.replace(";", "")
    content = content.replace("!", "")
    content = content.replace(",", " ")
    content = content.split(" ")
    for i in content:
        length = len(i)
        if length > longest:
            word = i
            longest = length
    return word , longest




def main():
    word , longest  = get_longest_word()
    print(f"Longest word is {word} wich is {longest} letters long")


main()