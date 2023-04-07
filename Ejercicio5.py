print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("30/03/2023")

sueldo=int(input("Ingrese sueldo: "))
impuesto=0
if sueldo<10000:
    impuesto=5/100
    print("El porcentaje de impuesto a pagar es 5%")
elif sueldo>=10000 and sueldo<=20000:
    impuesto=15/100
    print("El porcentaje de impuesto a pagar es 15%")
elif sueldo>=20000 and sueldo<=35000:
    impuesto=20/100
    print("El porcentaje de impuesto a pagar es 20%")
elif sueldo>=35000 and sueldo<=60000:
    impuesto=30/100
    print("El porcentaje de impuesto a pagar es 30%")

else:
    impuesto=45/100
    print("El porcentaje de impuesto a pagar es 45%")