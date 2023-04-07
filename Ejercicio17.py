print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("02/04/2023")

nota=float(input("Ingrese la nota: "))
if nota >= 0 and nota <= 2:
    print(f"Nota de {nota} muy deficiente")
elif nota >= 3 and nota <= 4:
    print(f"Nota de {nota} insuficiente")
elif nota >= 5 and nota <= 6:
    print(f"Nota de {nota} suficiente")
elif nota == 7:
    print(f"Nota de {nota}  bien")
elif nota >= 8 and nota <= 9:
    print(f"Nota de {nota} es notable")
elif nota == 10:
    print(f"Nota de {nota} es sobresaliente")
else:
    print(f"Nota de {nota} Error")