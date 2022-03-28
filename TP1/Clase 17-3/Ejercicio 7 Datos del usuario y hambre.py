#Que se le pida al usuario el nombre, la edad, el dinero que hay en su billetera y el hambre que tiene (medido de 0 a 10). Luego que muestre el mensaje:
#         Si es menor de 35: Hola - nombre -. Eres una persona joven ya que tu edad es -
#        edad.
#         Si es mayor a 34 y tiene más de $500 y su hambre es mayor a 5: Hola - nombre –
#        apellido- ¿Hoy hay asado?
#         Si su hambre es de al menos 7 o tiene menos de $100 y su edad es menor a 18: Hola -
#        nombre – apellido - ¿Vas a comer a lo de tus padres?"""



for i in range (1):
  nombre = input("\nIngrese su Nombre: ")
  apellido = input("\nIngrese Su Apellido: ")
  edad = float(input("\nIngrese su Edad: "))
  dinero  =float(input("\nIngrese el dinero que hay en su billetera: "))
  hambre = int(input("\n¿Cuanto hambre tiene del 1 a 10? "))

if edad < 35 and edad > 18:
    print(f"Hola {nombre} " "Eres una persona joven ya que tu edad es: ",edad)
elif edad >= 34 and dinero >= 500 and hambre > 5:
    print(f"Hola {nombre} {apellido}" " ¿Hoy hay asado?\n")
elif (hambre > 7 and dinero < 100 and edad < 18):
    print(f"Hola {nombre} {apellido}" " ¿Vas a comer en lo de tus Papas\n")