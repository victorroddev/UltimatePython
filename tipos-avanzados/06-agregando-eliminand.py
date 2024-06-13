mascotas = [
    "Wolfgang",
    "Pelusa", 
    "Pulga", 
    "Felipe",
    "Pulga", 
    "Chanchito feliz"
]

mascotas.insert(1, "Melvin") #Sustituir un elemento con el metodo insert
mascotas.append("Chanchito triste") #Agregar un elemento al final de la lista

mascotas.remove("Pulga") #Solo elmina el primer elemento de coincidencia
print(mascotas)
mascotas.pop()
print(mascotas)
mascotas.pop(1) #podemos tambien indicarle el indice de un elemento a eliminar
del mascotas[0] #con esta sintaxis tambien podemos eliminar con el indice
mascotas.clear() #limpiar una lista

