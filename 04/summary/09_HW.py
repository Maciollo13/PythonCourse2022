# Poproś 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
l1 = []
l2 = []
user1 = input("Input 4 school subject: ")
user2 = input("Input 4 school subject: ")
user3 = input("Input 4 school subject: ")
user4 = input("Input 4 school subject: ")
user5 = input("Input 4 school subject: ")
user1 = user1.lower()
user1 = user1.replace(",", "")
user2 = user2.replace(",", "")
user2 = user2.lower()
user3 = user3.replace(",", "")
user3 = user3.lower()
user4 = user4.replace(",", "")
user4 = user4.lower()
user5 = user5.replace(",", "")
user5 = user5.lower()
sub1 = user1.split()
sub1.extend(user2.split())
sub1.extend(user3.split())
sub1.extend(user4.split())
sub1.extend(user5.split())
repeated_subject = []
for i , v in enumerate(sub1):
    sub1.count(v)


print(sub1)