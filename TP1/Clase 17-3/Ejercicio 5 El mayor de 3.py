#El mayor de 3

a = int(input("\nIngrese un número del 1 al 100: "))
b = int(input("\nIngrese un número del 1 al 100: "))
c = int(input("\nIngrese un número del 1 al 100: "))

if a > b and a > c:
    print (f"{a} es mayor que {b} y {c}")
elif b > a and b > c:
    print (f"{b} es mayor que {a} y {c}")
elif c > a and c > b:
    print (f"{c} es mayor que {a} y {a}")
else:
    print ("El número ingresado es incorrecto")