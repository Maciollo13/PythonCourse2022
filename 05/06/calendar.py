def days(list_month):
    print(list_month[0])
    for day in list_month[1]:
        day += 1
        if day < 10:
            day = "0" + str(day)
        if int(day) % 7 == 0 and day != 0:
            print(day)
        else:
            print(day, end= " ")


def month(data , number):
    return list(data[number])


def main(data):
    number = int(input("Ktory miesiac wybierasz? "))
    number -= 1
    list_month = month(data,number)
    print(list_month)
    print(days(list_month))




data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]
main(data)
