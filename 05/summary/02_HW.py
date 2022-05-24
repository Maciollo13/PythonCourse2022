def min_of_2(a,b):
    if a < b:
        return a
    else:
        return b

def minimum_of(a, b):
    if a < b:
        return a
    else:
        return b
def main():
    first = (int(input("Podaj cyfrę ")))
    second = (int(input("Podaj cyfrę ")))
    third = (int(input("Podaj cyfrę ")))
    result1 = min_of_2(first, second)
    result = minimum_of(result1, third)
    print(result)



main()