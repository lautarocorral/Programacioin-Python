#Si una de las materias esta aprobada pero no promociona va a rendir final
#Lengua, matemática, física: Elegir las materias para cargar datos:
#Calcular el promedio de estas materias
#Si las materias tienes mayor promedio que 8 promociona
#Si las materias tienen menor 8 pero mayor igual a 6 aprueba
#Si las materias tienen menor que 6 desaprueban
#Sicl
#Si una de las materias está aprobada pero no promociona va a rendir final


Lengua = 1
Matematica = 2
Fisica = 3
Química = 4
Salir = 0
a = 0
nota1_l = []
nota2_l = []
nota3_l = []

nota1_m = []
nota2_m = []
nota3_m = []

nota1_f = []
nota2_f = []
nota3_f = []

nota1_q = []
nota2_q = []
nota3_q = []
print("Selecione el numero correspondiente a la materia:\n1=> Lengua\n2=> Matemática\n3=> Física\n4=> Química\n0=> Salir")


while a <= 3:
    materia = int(input("\nIngrese una materia: "))
   
    if materia == 1 :
        nota1_l = float(input("ingrese nota1: "))
        nota2_l = float(input("ingrese nota2: "))
        nota3_l = float(input("ingrese nota3: "))

        suma = (nota1_l +nota2_l +nota3_l)
        promedio1 = suma/3
        print(f"su promedio es de {promedio1}")
        if promedio1 >= 8:
            print("PROMOCIONADO")
        elif promedio1 >= 6:
            print("Aprobado")
        elif promedio1 < 6:
            print ("Desaprobado")

    elif materia == 2 :
        nota1_m = float(input("ingrese nota1: "))
        nota2_m = float(input("ingrese nota2: "))
        nota3_m = float(input("ingrese nota3: "))

        suma = (nota1 +nota2 +nota3)
        promedio2= suma/3
        print(f"su promedio es de {promedio2}")
        if promedio2 >= 8:
            print("PROMOCIONADO")
        elif promedio2 >= 6:
            print("Aprobado")
        elif promedio2 < 6:
            print ("Desaprobado")

    elif materia == 3 :
        nota1_f = float(input("ingrese nota1: "))
        nota2_f = float(input("ingrese nota2: "))
        nota3_f = float(input("ingrese nota3: "))

        suma = (nota1 +nota2 +nota3)
        promedio3= suma/3
        print(f"su promedio es de {promedio3}")
        if promedio3 >= 8:
            print("PROMOCIONADO")
        elif promedio3 >= 6:
            print("Aprobado")
        elif promedio3 < 6:
            print ("Desaprobado")
    
    elif materia == 4 :
        nota1_q = float(input("ingrese nota1: "))
        nota2_q = float(input("ingrese nota2: "))
        nota3_q = float(input("ingrese nota3: "))

        suma = (nota1 +nota2 +nota3)
        promedio4 = suma/3
        print(f"su promedio es de {promedio4}")
        if promedio4 >= 8:
            print("PROMOCIONADO")
        elif promedio4 >= 6:
            print("Aprobado")
        elif promedio4 < 6:
            print ("Desaprobado")
        
    else: 
        print ("El número ingresado es incorrecto")
    a += 1    #contador de materias
   
# 4 PROMEDIOS IGUALES
if promedio1 >= 8 and promedio2 >= 8  and promedio3 >= 8 and promedio4 >= 8:
    print ("Felicitaciones, a promocionado las 3 materias")
elif   (promedio1 >= 6 and promedio1 < 8) and (promedio2 >= 6 and promedio2 < 8)  and (promedio3 >= 6 and promedio3 < 8) and (promedio4 >= 6 and promedio4 < 8):
    print ("Aprobado, pero no te alcanzo, vas a tener que rendir finales de las 4 materias")  
elif promedio1 < 6 and promedio2 < 6 and promedio3 < 6 and promedio4 < 6:
    print ("Debe rendir denuevo las 3 materias")

#PROMOCiON
if promedio1 >= 8:
    print ("Felicitaciones, a promocionado Lengua")
elif promedio2 >= 8:
    print ("Felicitaciones, a promocionado Matemática")
elif promedio3 >= 8:
    print ("Felicitaciones, a promocionado Física")
elif promedio4 >= 8:
    print ("Felicitaciones, a promocionado Química")

#APROBADO
if promedio1 >= 6 and promedio1 < 8:
    print ("Aprobado, pero no te alcanzo, vas a tener que rendir final de Lengua")
elif promedio2 >= 6 and promedio2 < 8:
    print ("Aprobado, pero no te alcanzo, vas a tener que rendir final de Matemática")
elif promedio3 >= 6 and promedio3 < 8:
    print ("Aprobado, pero no te alcanzo, vas a tener que rendir final de Física")
elif promedio4 >= 6 and promedio4 < 8:
    print ("Aprobado, pero no te alcanzo, vas a tener que rendir final de Química")

#DESAPROBADO
if promedio1 < 6:
    print ("Desaprobado, vas a tener que cursar Lengua de nuevo")
elif promedio2 < 6:
    print ("Desaprobado, vas a tener que cursar Matemática de nuevo")
elif promedio3 < 6:
    print ("Desaprobado, vas a tener que cursar Física de nuevo")
elif promedio4 < 6:
    print ("Desaprobado, vas a tener que cursar Química de nuevo")
