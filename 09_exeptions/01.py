l1 = [13, "hello", 3.14, True, None, [12, 4],0]
for i in l1:
    try:
        result = 10/i
        print(result)
    except TypeError:
        print(f"10/{i} NIe moge wykonać")
    except ZeroDivisionError:
        print(f"10/{i} Nie dziel przez 0")