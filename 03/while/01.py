# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
tempC = 0
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
temp = 0
while temp >= 0 and temp <= 200:
    tempC = 5/9 * (temp - 32)
    print(round(tempC, 2))
    temp += 20