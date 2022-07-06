import time

def timer(func):
    def timing():
        start_time = time.time()
        func()
        print(time.time()- start_time)
    return timing

def uppercase(func):
    def upperc():
        return func().upper()
    return upperc
@timer
@uppercase
def string_user():
    return "sentence"

def main():
    string_user()

if __name__ == "__main__":
    main()