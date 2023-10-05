from tp5_funciones import*
#Ejercicio 1

"""while True:
    try:
        dni=int(input("Ingresa tu DNI: "))
        break
    except ValueError:
        print("El valor ingresado no es numerico")
        continue
print(ciclingdni(dni))"""

#Ejercicio 2

"""words = input("Ingrese un String: ")
longstring(lastword(words))
"""
#ejercicio3
"""print("Puede ingresar más de un nombre y al final el apellido. Si tuviera más de un apellido, ingrese uno.")
fullname = input("Ingresa tu nombre completo: ").title()
while True:
    while True:
        try:
            dni=int(input("Ingresa tu DNI: "))
            break
        except ValueError:
            print("El valor ingresado no es numerico")
            continue
    if(ciclingdni(dni)):
        break
    else:
        print("Este número no tiene 7 u 8 digitos")

print(f"Nombre: {fullname} \nDNI:{dni} \nID: {identificador(fullname,dni)}")
"""
#Ejercicio 4

"""number1 = int(input("Ingresa un número: "))
number2 = int(input("Ingresa otro número: "))
multiplo(number1,number2)
multiplo(number2,number1)"""

#Ejercicio 5

"""days=int(input("Cantidad de días a introducir:\n"))
for i in range(days):
    print(f"Día: {i+1}")
    tempmax=int(input("Ingresa la temperatura máxima: "))
    tempmin=int(input("Ingresa la temperatura mínima: "))
    print(f"La temperatura media del dia es de {medium(tempmax,tempmin)}°C")
"""
#Ejercicio 6

"""words = input("Ingresa un texto:\n")
print(spacebetween(words))"""

#Ejercicio 7
#
a=[]

while True:
    try:
        quantity = int(input("¿Cuántos numeros quieres ingresar?\n"))
        break
    except ValueError:
        print("El valor ingresado no es numérico")
        continue
for i in range(quantity):
    while True:
        try:
            number = int(input(f"{i+1}: "))
            break
        except ValueError:
            print("El valor ingresado no es numérico")
            continue
    a.append(number)

max_min_num(a)

