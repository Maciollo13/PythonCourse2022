class Pen:
    def show_description(self):
        print("Pen is used to write things")



class Pineapple:
    def taste(self):
        print('Pineapple is sweet in taste')

class PenPineapple(Pen,Pineapple):
    def __init__(self):
        print("Apple Pineapple")
    def show_lyric(self):
        print("PenPineapple apple pen")
    def summary(self):
        super().show_description()
        super().taste()



if __name__ == "__main__"
    P = Pen()
    apple = Pineapple()
    papple = PenPineapple()
    papple.show_lyric()
