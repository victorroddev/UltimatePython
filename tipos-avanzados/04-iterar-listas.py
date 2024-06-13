mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]



for mascota in mascotas: # iteramos e imprimimos mascotas por cada iteracion
    print(mascota)

for indice, mascota in enumerate(mascotas): #iteramos pero obtenemos tambien el indice de los elementos
    print(indice, mascota)