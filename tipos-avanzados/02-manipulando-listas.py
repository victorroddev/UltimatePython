mascotas = ["Wolfgang", "Pelusa", "Copito"]
print(mascotas)
print(mascotas[0]) #Accedemos a un elemento de la lista por el indice
mascotas[0] = "Bicho" #Cambiamos un elemento con su indice
print(mascotas)
print(mascotas[0:3]) #Obtener una parte parcial de la lista
#En esta sintaxis el indice de la izquierda es donde se inicia a tomar elementos de la lista y el de la derecha en donde termina.
###############################################################
print(mascotas[::2]) #Con esta sintaxis le estamos indicando que tome un elemento el siguiente lo sale, que tome otro y el siguiente lo salte


numeros = list(range(21))
print(numeros)
print(numeros[::2]) #imprimimos numeros pares
print(numeros[1::2]) #Imprimimos numeros impares