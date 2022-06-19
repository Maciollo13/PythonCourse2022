def get_index():
    index = int(input("Podaj index -> "))
    return index

def main():
    l1 = [13, "hello", 3.14, True, None, [12, 4], 0]
    index = get_index()
    try:
        result = 1/l1[index]
        print(result)
    except TypeError:
        print(f"1/{index} Nie moge wykonać")
    except ZeroDivisionError:
        print(f"1/{index} Nie dziel przez zero")
    except IndexError:
        print(f"Nie ma indexu {index}")


if __name__ == "__main__":
    main()