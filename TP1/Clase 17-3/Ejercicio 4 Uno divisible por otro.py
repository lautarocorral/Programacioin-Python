a = int(input("\nIngrese el primer número: "))
b = int(input("\nIngrese el segundo número: "))
if a % b == 0:
    print (f"{a} es divisible por {b}")
    print (f"El resultado es : {a / b}")
    
else:
    print(f"{a} NO es divisible por {b}") 
    print (f"El resultado es : {a / b}")