class pies:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def how(self):
        return f"{self.name} - How How"

    def tail_whip(self):
        return f"{self.name} whips his tail"


tuptus = pies("Tuptuś", "black", "Jamnik")
benek = pies("Benek", "Grey", "Kundel")
print(tuptus.how())
print(benek.tail_whip())