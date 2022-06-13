import BMI

def get_advise(result):
    print(f"You have {result}.")
    result = result.replace(" ", "")
    result = result.lower()
    print(result)
    with open(f"{result}.txt") as fopen:
        advise = fopen.read()
    return advise



def main():
    weight = (input("Input your weight: "))
    height = (input("Input your height in cm: "))
    result = BMI.BMI_counter(weight, height)
    print(get_advise(result))

if __name__ == "__main__":
    main()