# Realizar una calculadora con operaciones básicas. Se debe validar que el usuario siempre ingrese valores numéricos.

operacion = 0

print ("\nCalculadora básica\n")

while operacion != 9:
    print("1=> Suma\n2=> Resta\n3=> División\n4=> Multiplicación\n9=> Salir")
    operacion = float(input("Selecione el numero correspondiente a la operación:\n\n"))
    if operacion == 1:
        print("\nHa elegido Suma")
        a = float(input("Ingrese el primer valor: \n"))
        b = float(input("Ingrese el segundo valor: \n"))
        suma = (a + b)
        print (f"\nEl resultado es : {suma}\n" )
    elif operacion == 2:
        print("\nHa elegido Resta")
        a = float(input("Ingrese el primer valor: \n"))
        b = float(input("Ingrese el segundo valor: \n"))
        resta = (a - b)
        print (f"\nEl resultado es : {resta}\n" )
    elif operacion == 3:
        print("\nHa elegido División")
        a = float(input("Ingrese el primer valor: \n"))
        b = float(input("Ingrese el segundo valor: \n"))
        division = (a / b)
        print (f"\nEl resultado es : {division}\n" )
    elif operacion == 4:
        print("\nHa elegido Multiplicación")
        a = float(input("Ingrese el primer valor: \n"))
        b = float(input("Ingrese el segundo valor: \n"))
        multiplicacion = (a * b)
        print (f"\nEl resultado es : {multiplicacion}\n" )
    elif operacion == 9:
        print ("\nHa ingresado la opcion SALIR\nHASTA PRONTO")


