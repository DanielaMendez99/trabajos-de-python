print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("31/03/2023")

d=int(input("Ingrese 1er valor: "))
e=int(input("Ingrese 2do valor: "))
f=int(input("Ingrese 3er valor: "))

if d>e and d>f:
    print("El numero mayor es",d)
elif e>d and e>f:
    print("El numero mayor es",e)
elif f>d and f>e:
    print("El numero mayor es",f)