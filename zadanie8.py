print("Wszystkie wymiary muszą być w cm")
a = int(input("Podaj wymiar a: "))
b = int(input("podaj wymiar b: "))
c = int(input("Podaj wymiar h: "))

v = (a*b*c) > 1000
print(str(v))