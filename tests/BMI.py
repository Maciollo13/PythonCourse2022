class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculator(self):
        return self.weight/(self.height**2)
