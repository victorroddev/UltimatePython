usuarios = [
    ["Chancito", 4],
    ["Felipe", 1],
    ["Pulga", 5] 
]

nombres = []

# for usuario in usuarios: #for para obtener solo los nombres con metodo append
#     nombres.append(usuario[0])

nombres = [usuario[0] for usuario in usuarios] #Mismo resultado con diferente sintaxis
#filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


print(nombres)