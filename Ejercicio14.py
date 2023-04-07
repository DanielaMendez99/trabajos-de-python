print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("31/03/2023")

numero=int(input("Ingresar una cantidad: "))

if numero%4==0 and numero%6==0:
    print(numero, "es divisible para4 y 6.")
else:
    print(numero, "no es divisible para 4 y 6.")