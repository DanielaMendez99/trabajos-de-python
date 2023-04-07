print("FUNDAMENTOS DE PROGRAMACION EN PYTHON")
print("Daniela Mendez")
print("30/03/2023")

#La pizzería Bella Napoli ofrece pizzas Hawaiana y no Hawaiana a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes Hawaiana: Piña y Peperoni.
#Ingredientes no Hawaiana: Jamón y Tofu

print('\n\tPizzería Napolitana\n\n\tMenú de Pizzas\n1.Pizzas Hawaiana \n2.Pizzas no Hawaiana')
opción=int(input('Ingrese una opción del menú: '))
if opción==1:
    print('\tUsted eligio el tipo de pizzas Hawaiana\nLos ingredientes disponibles son:\n1.Piña\n2.Peperoni\n Solo puede elegir un ingrediente!!!')
    ingredientev=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientev==1:
        print('Su pizza consta de Piña,mozzarella y Jamon!!')
    elif ingredientev==2:
        print('Su pizza consta de Piña,mozzarella y Jamon!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')
elif opción==2:
    print('\tUsted eligio el tipo de pizzas no Hawaiana\nLos ingredientes disponibles son:\n1.Peperoni\n2.piña\ntofu\nSolo puede elegir un ingrediente!!!')
    ingredientesn=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientesn==1:
        print('Su pizza consta de Peperoni,tofu y piña!!')
    elif ingredientesn==2:
        print('Su pizza consta de Peperoni,tofu y piña!!')
    elif ingredientesn==3:
        print('Su pizza consta de Peperoni,tofu y piña!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')