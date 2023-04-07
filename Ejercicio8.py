print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("31/03/2023")

numero=input("Ingrese un numero: ")
if len(numero) !=1:
    print("No se puede procesar el dato, debe ingresar un solo numero")
elif numero in "123456789":
    print("El numero",numero, "se encuentra dentro del rango")
else: 
    print("El numero ingresado no se encuntra dentro del rango")

abecedario= input("Ingrese una letra: ")
abecedario=abecedario.lower()

if len(abecedario) != 1:
    print("No se puede procesar el dato. Debe ingresar una sola letra.")
elif abecedario in "abcdefghijklmnopqrstuvwxyz":
    print("Pertenece al abecedario")
    
else:
    print("No es una letra") 