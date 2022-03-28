#Nombre de amigos
#Mostrar todos los nombres de amigos concatenados con un guion ( - ).

#nombres = ["a","b","c","d","e","f","g"]

#nombres = str(input("Ingrese 5 nombres de sus amigos cercanos: \n"))

#print (f"Estos son mis amigos:\n\n{nombres}\n")

# n = nombres

n = []
print ("Cuantos nombres quieres escribir")
cantidadn = int(input())
i = 0
while i < cantidadn:
    print ("Ingrese el nombre de uno de sus amigos" ,i + 1 )
    nombre = (input())
    n.append (nombre)
    i += 1
n.sort()
print (*n, sep="-")



#n.append(input("Ingrese nombres de sus amigos cercanos: \n"))
#print (f"{n} amigos")
