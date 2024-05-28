# calculadora


print("Bienvenidos a la calculadora\n Para salir escribe Salir\n las operaciones son suma, multi, div y resta")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese primer numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es {resultado}")
