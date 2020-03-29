a = float(input("Podaj liczbę: "))
b = float(input("Podaj liczbę: "))

print("Podaj jaką operację chcesz wykonać: -, +, :, * ")

znak = str(input("Podaj znak działania: "))

if znak == "+" :
    print(a + b)
if znak == "-":
    print(a-b)
if znak == ":":
    print(a/b)
if znak == "*":
    print(a*b)
else:
    print("Podałeś zły znak")