print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("31/03/2023")

año=int(input("Ingresar el año: "))
if año%600==0:
    print("El año es bisiesto")
elif año%200==0:
    print("El año no es bisiesto")