import datetime

born = int(input("Podaj rok urodzenia: "))
current_year = datetime.datetime.now().year

if (current_year - born) > 18:
    print("Jesteś pełnoletni/a")
else:
    print("Nie jesteś pełnoletni/a")

