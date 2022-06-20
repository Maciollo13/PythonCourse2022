def numbers_input():
    numbers = input("Write numbers divorced by \",\"")
    number_list = numbers.split(",")
    return number_list


def get_average(l1):
    summ = 0
    for i in l1:
        try:
            summ += int(i)
        except TypeError:
            with open("TypeError.txt", "a") as fopen:
                fopen.write("TypeError \n")
        except ValueError:
            with open("ValueError.txt", "a") as fopen:
                fopen.write("ValueError \n")
    try:
        avg = summ/len(l1)
    except TypeError:
        pass
    return avg



def main():
    l1 = numbers_input()
    avg = get_average(l1)
    print(avg)


main()