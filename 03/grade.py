num = 0
sum_grades = 0
subject = ""
grade = ""
while num <= 3:
    subject = (input("podaj przedmiot szkolny"))
    grade = input("Podaj ocene")
    print(f"Z przedmiotu {subject} uzyskałeś ocenę {grade} ")
    num += 1
    sum_grades += grade
avrage = sum_grades/3
