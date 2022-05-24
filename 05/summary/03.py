def max_of_2(a,b):
    if a > b:
        return a
    else:
        return b

def maximum_of(a, b):
    if a > b:
        return a
    else:
        return b
def main():
    a = (int(input("Podaj cyfrę ")))
    b = (int(input("Podaj cyfrę ")))
    c = (int(input("Podaj cyfrę ")))
    result1 = max_of_2(a, b)
    result = maximum_of(result1, c)
    print(result)



main()