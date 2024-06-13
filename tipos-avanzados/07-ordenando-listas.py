numeros = [2,4,1,45,75,22]

numeros.sort() #ordenamos nuestra lista
print(numeros)
numeros.sort(reverse=True) #ordenamos la lista en reversa
print(numeros)

numeros2 = sorted(numeros) #Este metodo ordena pero devuelve una lista nueva
numeros2 = sorted(numeros, reverse=True) #Este metodo ordena en reversa
print(numeros)
print(numeros2)


usuarios = [
    ["Chancito", 4],
    ["Felipe", 1],
    ["Pulga", 5] 
]

def ordena(elemento): #funcion para ordenar elemento
    return elemento[1]

usuarios.sort(key=ordena) #sintaxis para poder ordenar aunque el primer elemento no sea ordenable


usuarios.sort(key=lambda el:el[1]) #Sintaxis lambda que hace lo mismo de arriba

print(usuarios)