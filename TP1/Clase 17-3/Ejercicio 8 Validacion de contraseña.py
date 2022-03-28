"""#Escriba un programa que solicite el apellido, nombre, año de nacimiento y contraseña, con las siguientes validaciones:
""" # El nombre y apellido debe tener al menos 3 vocales.
    # El año de nacimiento debe ser un formato correcto: contener solo números y cuatro dígitos.
    # La contraseña tiene que tener como mínimo 8 caracteres y un máximo de 16.
    # La contraseña al menos debe contener un carácter especial: ! “ # $ % & . -
#Una vez ingresado correctamente todos los valores. Se debe saludar al usuario con su nombre y apellido.



print ("\nValidación de usuario\n")
print ("A continuación se le pedira su nombre y apellido.\nRecuerde que estos deben de tener en cada uno al menos 3 vocales.\n")

nombre = str(input("Ingrese su nombre: \n"))

apellido = str(input("Ingrese su apellido: \n"))

año = int(input("Ingrese su fecha de nacimiento: \n"))

print (nombre, apellido, año)






    