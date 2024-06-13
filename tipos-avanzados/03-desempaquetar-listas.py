numeros = [1,2,3]


#feo
# primero = numero[0]
# segundo = numero[1]
# tercero = numero[2]

# primero, segundo, tercero = numeros #sintaxis para obtener todos lo elementos de un listado
# print(primero,segundo,tercero)

# primero, *otros = numeros #De esta forma obtenemos solo el primer elemento del listado
# print(primero, otros)

numeros = [1,2,3,4,5,6,7,8,9]
primero, *otros, ultimo = numeros #Sintaxis para obtener el primero y el ultimo elemento
primero, segundo, *otros, penu, ultimo = numeros #sintaxis para obtener segundo y penultimo elemento
print(primero, ultimo, otros)