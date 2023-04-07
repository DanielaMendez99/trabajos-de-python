print("FUNDAMENTOS DE PYTHON")
print("Daniela Mendez")
print("3/30/2023")

estado=input("Ingrese estado del semaforo: ")


if estado=="verde":
    print("Puede cruzar la calle")
elif estado=="amarillo":
    print("Por favor detengase")
elif estado=="rojo":
    print("No puede cruzar la calle")
else:
    print("El estado ingresado es incorrecto")