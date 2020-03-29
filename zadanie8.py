print("Wszystkie wymiary muszą być w cm")
a = int(input("Podaj wymiar a: "))
b = int(input("podaj wymiar b: "))
c = int(input("Podaj wymiar h: "))

v = a * b * c
x = v > 1000
print("Objetosc wynosi: " + str(v))
print("Objetosc jest wieksza niz 1 litr; " + str(x))
