# Realizar un juego donde el usuario debe adivinar el número arrojado por la función random. Solamente cuenta con 5 intentos
import random
numero = ()
n = ()
print ("\nAdivina adivinador\n\nIngresa un numero del 1 al 10\n¡¡¡Pero cuidado, solo tienes 5 intentos!!!\n")

for i in range (0,5) :
    
    numero = int(input("\nIngresa tu número\n"))
    n = random.randrange(0,10)
    print (n)
    
    if numero == n:
        print ("\n¡FELICITACIONES!\nLo has logrado")    
    elif numero > 10:
        print ("\nEl numero ingresado es mayor al permitido")
    elif numero != n:
        print ("\nSeguí participando")
    else:
        print ("ERROR")
    if numero == n:
        break
